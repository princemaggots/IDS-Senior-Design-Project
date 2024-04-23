import numpy as np
import time
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from skopt import gp_minimize
from skopt.space import Integer
from skopt.utils import use_named_args
from hyperopt import hp, fmin, tpe, STATUS_OK, Trials

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def cl_kmeans(X_train, X_test, y_train, y_test, n_clusters=8, batch_size=100):
    """
    Cluster Labeling with K-Means: Assigns labels based on the majority class within each cluster.
    """
    km_cluster = MiniBatchKMeans(n_clusters=n_clusters, batch_size=batch_size)
    result_train = km_cluster.fit_predict(X_train)
    result_test = km_cluster.predict(X_test)

    # Initialize counts
    a = np.zeros(n_clusters)
    b = np.zeros(n_clusters)

    # Count class occurrences
    for v in range(n_clusters):
        for i in range(len(y_train)):
            if result_train[i] == v:
                if y_train[i] == 1:
                    a[v] += 1
                else:
                    b[v] += 1

    # Determine majority class for each cluster
    list1, list2 = [], []
    for v in range(n_clusters):
        if a[v] <= b[v]:
            list1.append(v)
        else:
            list2.append(v)

    # Assign labels to test set
    for v in range(len(y_test)):
        if result_test[v] in list1:
            result_test[v] = 0
        elif result_test[v] in list2:
            result_test[v] = 1

    # Reporting
    print(classification_report(y_test, result_test))
    cm = confusion_matrix(y_test, result_test)
    acc = accuracy_score(y_test, result_test)
    print("Accuracy:", acc)
    print("Confusion Matrix:")
    print(cm)

def hyperopt_gp(X_train, y_train):
    """
    Hyperparameter Optimization using Gaussian Process (GP) through scikit-optimize.
    """
    space = [Integer(2, 50, name='n_clusters')]

    @use_named_args(space)
    def objective(**params):
        km_cluster = MiniBatchKMeans(batch_size=100, **params)
        result_train = km_cluster.fit_predict(X_train)
        # Simplified objective function: optimizes for the silhouette score
        from sklearn.metrics import silhouette_score
        score = silhouette_score(X_train, result_train)
        return -score  # maximize score

    t_start = time.time()
    res_gp = gp_minimize(objective, space, n_calls=20, random_state=0)
    t_end = time.time()
    print("Optimization Time:", t_end - t_start)
    print("Best score=%.4f" % (-res_gp.fun))
    print("Best parameters: n_clusters=%d" % (res_gp.x[0]))

def hyperopt_tpe(X_train, y_train):
    """
    Hyperparameter Optimization using Tree-structured Parzen Estimator (TPE).
    """
    space = {
        'n_clusters': hp.quniform('n_clusters', 2, 50, 1)
    }

    def objective(params):
        n_clusters = int(params['n_clusters'])
        km_cluster = MiniBatchKMeans(batch_size=100, n_clusters=n_clusters)
        result_train = km_cluster.fit_predict(X_train)
        # Simplified objective function: optimizes for the silhouette score
        from sklearn.metrics import silhouette_score
        score = silhouette_score(X_train, result_train)
        return {'loss': -score, 'status': STATUS_OK}

    best = fmin(fn=objective, space=space, algo=tpe.suggest, max_evals=20)
    print("Best hyperparameters:", best)


def build_biased_classifiers(df, cluster_results, labels, n_clusters):
    """
    Builds biased classifiers based on cluster results.
    """
    a = np.zeros(n_clusters)
    b = np.zeros(n_clusters)
    FNL = []
    FPL = []

    # Determine the majority class for each cluster
    for i in range(len(labels)):
        cluster_id = cluster_results[i]
        if labels[i] == 1:
            a[cluster_id] += 1
        else:
            b[cluster_id] += 1

    # Assign indices to biased datasets
    for v in range(n_clusters):
        al = []
        bl = []
        for i in range(len(labels)):
            if cluster_results[i] == v:
                if labels[i] == 1:
                    al.append(i)
                else:
                    bl.append(i)
        if a[v] <= b[v]:
            FNL.extend(al)
        else:
            FPL.extend(bl)

    # Create dataframes for biased classifiers
    dffp = df.iloc[FPL]
    dffn = df.iloc[FNL]
    dfva1 = df[df['Label'] == 1]
    dfva0 = df[df['Label'] == 0]

    dffpp = dfva1.sample(n=len(FPL), replace=False, random_state=None) if len(dfva1) > 0 else pd.DataFrame()
    dffnp = dfva0.sample(n=len(FNL), replace=False, random_state=None) if len(dfva0) > 0 else pd.DataFrame()

    dffp_final = pd.concat([dffp, dffpp])
    dffn_final = pd.concat([dffn, dffnp])

    # Train Random Forest classifiers
    rfp = train_random_forest(dffp_final.drop('Label', axis=1), dffp_final['Label'])
    rfn = train_random_forest(dffn_final.drop('Label', axis=1), dffn_final['Label'])

    # Return the trained classifiers
    return rfp, rfn

def train_random_forest(X, y):
    """
    Trains a RandomForestClassifier on provided data.
    """
    classifier = RandomForestClassifier(random_state=0)
    classifier.fit(X, y)
    return classifier

def reevaluate_clusters(classifiers, df, cluster_results):
    """
    Reevaluates data based on the trained biased classifiers.
    """
    predictions = []
    for index, row in df.iterrows():
        cluster_id = cluster_results[index]
        model = classifiers[0] if cluster_id in [0] else classifiers[1]  # Example split
        pred = model.predict(row.drop('Label').values.reshape(1, -1))
        predictions.append(pred[0])

    # Print classification report
    print(classification_report(df['Label'], predictions))
    print("Confusion Matrix:")
    print(confusion_matrix(df['Label'], predictions))

