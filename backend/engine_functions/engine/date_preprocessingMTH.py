import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import mutual_info_classif
from engine_functions.engine.FCBF_module.FCBF_module import FCBFK  # Assuming FCBF module provides the FCBFK class

def preprocess_data(filepath, test_size, feature_selection_threshold, fcbf_k):
    # Read the sampled dataset
    df=pd.read_csv(filepath)
    features = df.dtypes[df.dtypes != 'object'].index # added
    X = df.drop(['Label'],axis=1).values
    y = df.iloc[:, -1].values.reshape(-1,1)
    y=np.ravel(y)
    train_size = 1 - test_size
    X_train, X_test, y_train, y_test = train_test_split(X,y, train_size = train_size, test_size = test_size, random_state = 0,stratify = y)

    # importances = mutual_info_classif(X_train, y_train)
    # f_list = sorted(zip(map(lambda x: round(x, 4), importances), features), reverse=True)
    # Sum = 0
    # fs = []
    # for i in range(0, len(f_list)):
    #     Sum = Sum + f_list[i][0]
    #     fs.append(f_list[i][1])
    # f_list2 = sorted(zip(map(lambda x: round(x, 4), importances/Sum), features), reverse=True)
    # Sum2 = 0
    # fs = []
    # for i in range(0, len(f_list2)):
    #     Sum2 = Sum2 + f_list2[i][0]
    #     fs.append(f_list2[i][1])
    #     if Sum2>=0.9:
    #         break  
    # X_fs = df[fs].values
    # fcbf = FCBFK(k = fcbf_k)
    # print(type(X_fs))
    # print(type(y))
    # X_fss = fcbf.fit_transform(X_fs,y)
    # X_train, X_test, y_train, y_test = train_test_split(X_fss,y, train_size = train_size, test_size = test_size, random_state = 0,stratify = y)


    return df, X_train, X_test, y_train, y_test

# def normalize_features(df):
#     """Apply Z-score normalization to numerical features."""
#     features = df.select_dtypes(include=[np.number]).columns.tolist()
#     df[features] = df[features].apply(lambda x: (x - x.mean()) / x.std())
#     df = df.fillna(0)
#     return df

# def encode_labels(df):
#     """Encode categorical labels using LabelEncoder."""
#     labelencoder = LabelEncoder()
#     df.iloc[:, -1] = labelencoder.fit_transform(df.iloc[:, -1])
#     return df

# def balance_data(df):
#     """Balance the data by sampling the majority class after k-means clustering."""
#     df_minor = df[(df['Label'] == 6) | (df['Label'] == 1) | (df['Label'] == 4)]
#     df_major = df.drop(df_minor.index)
    
#     X = df_major.drop(['Label'], axis=1)
#     y = df_major['Label'].values.reshape(-1, 1)
#     y = np.ravel(y)
    
#     kmeans = MiniBatchKMeans(n_clusters=1000, random_state=0).fit(X)
#     df_major['klabel'] = kmeans.labels_
    
#     def typical_sampling(group):
#         frac = 0.008  # Proportion of data to sample from each cluster
#         return group.sample(frac=frac)
    
#     result = df_major.groupby('klabel', group_keys=False).apply(typical_sampling)
#     result = result.drop(['klabel'], axis=1)
#     result = result.append(df_minor)
    
#     return result

# def save_preprocessed_data(df, filepath):
#     """Save the preprocessed data to a CSV file."""
#     df.to_csv(filepath, index=False)

# def split_data(df):
#     """Split data into train and test sets."""
#     features = df.dtypes[df.dtypes != 'object'].index  # Ensure no object type features
#     X = df.drop(['Label'], axis=1).values
#     y = df.iloc[:, -1].values.reshape(-1, 1)
#     y = np.ravel(y)
#     X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0, stratify=y)
#     return X_train, X_test, y_train, y_test

# def main_preprocess(filepath):
#     """Main function to preprocess data."""
#     df = pd.read_csv(filepath)
#     df = normalize_features(df)
#     df = encode_labels(df)
#     df = balance_data(df)
#     X_train, X_test, y_train, y_test = split_data(df)
#     return X_train, X_test, y_train, y_test
