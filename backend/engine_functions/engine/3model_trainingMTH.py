# Import necessary libraries
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, DecisionTreeClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report, confusion_matrix
from hyperopt import hp, fmin, tpe, STATUS_OK, Trials
import matplotlib.pyplot as plt
import seaborn as sns

# Model training functions
def train_xgboost(X_train, y_train, params):
    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train, params):
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    return model

def train_decision_tree(X_train, y_train, params):
    model = DecisionTreeClassifier(**params)
    model.fit(X_train, y_train)
    return model

def train_extra_trees(X_train, y_train, params):
    model = ExtraTreesClassifier(**params)
    model.fit(X_train, y_train)
    return model

# Evaluate model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision, recall, fscore, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
    report = classification_report(y_test, y_pred)
    return accuracy, precision, recall, fscore, report

# Print evaluation results
def print_evaluation_results(accuracy, precision, recall, fscore, report):
    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1-Score: {fscore}')
    print("Classification Report:")
    print(report)

# Visualization
def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(5, 5))
    sns.heatmap(cm, annot=True, linewidth=0.5, linecolor="red", fmt=".0f")
    plt.xlabel("Predicted labels")
    plt.ylabel("True labels")
    plt.show()

# Hyperparameter optimization
def objective(params, X_train, y_train, X_test, y_test, model_type):
    if model_type == 'xgboost':
        model = train_xgboost(X_train, y_train, params)
    elif model_type == 'random_forest':
        model = train_random_forest(X_train, y_train, params)
    elif model_type == 'decision_tree':
        model = train_decision_tree(X_train, y_train, params)
    elif model_type == 'extra_trees':
        model = train_extra_trees(X_train, y_train, params)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return {'loss': -accuracy, 'status': STATUS_OK}

def optimize_hyperparams(X_train, y_train, X_test, y_test, model_type, space, max_evals=50):
    best = fmin(
        fn=lambda params: objective(params, X_train, y_train, X_test, y_test, model_type),
        space=space,
        algo=tpe.suggest,
        max_evals=max_evals
    )
    return best