import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_classif

def load_and_preprocess_data(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)
    print(df['Label'].value_counts())  # Output the distribution of the 'Label'

    # Separate data based on label
    df_non_portscan = df[df['Label'] != 5]
    df_non_portscan['Label'][df_non_portscan['Label'] > 0] = 1
    df_non_portscan.to_csv('./data/CICIDS2017_sample_km_without_portscan.csv', index=False)

    df_portscan = df[df['Label'] == 5]
    df_portscan['Label'][df_portscan['Label'] == 5] = 1
    df_portscan.to_csv('./data/CICIDS2017_sample_km_portscan.csv', index=False)

def read_and_normalize_features():
    # Read datasets
    df1 = pd.read_csv('./data/CICIDS2017_sample_km_without_portscan.csv')
    df2 = pd.read_csv('./data/CICIDS2017_sample_km_portscan.csv')

    # Normalize features
    features = df1.drop(['Label'], axis=1).dtypes[df1.dtypes != 'object'].index
    df1[features] = df1[features].apply(lambda x: (x - x.mean()) / (x.std()))
    df2[features] = df2[features].apply(lambda x: (x - x.mean()) / (x.std()))
    df1.fillna(0, inplace=True)
    df2.fillna(0, inplace=True)

    # Balancing the datasets by sampling
    df_non_attacks = df1[df1['Label'] == 0]
    df_sampled_non_attacks = df_non_attacks.sample(frac=1255/18225, replace=False, random_state=None)
    df_balanced = pd.concat([df2, df_sampled_non_attacks])

    # Combine and shuffle datasets
    final_df = pd.concat([df1, df_balanced], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
    return final_df

def select_features_by_importance(X, y, features, threshold=0.9):
    # Calculate mutual information
    importances = mutual_info_classif(X, y)
    
    # Calculate the sum of importance scores and select features
    total_importance = sum(importances)
    cumulative_importance = 0
    selected_features = []

    for importance, feature in sorted(zip(importances, features), reverse=True, key=lambda x: x[0]):
        cumulative_importance += importance / total_importance
        selected_features.append(feature)
        if cumulative_importance >= threshold:
            break

    return selected_features

def feature_selection_fcbf(X, y, k=20):
    # Assuming an FCBF implementation is available
    from FCBF_module import FCBFK
    fcbf = FCBFK(k=k)
    X_selected = fcbf.fit_transform(X, y)
    return X_selected

def prepare_datasets(df):
    # Split data into features and labels
    features = df.columns.drop('Label')
    X = df[features].values
    y = df['Label'].values.ravel()

    # Select features using mutual information
    selected_features = select_features_by_importance(X, y, features)
    X_fs = df[selected_features].values

    # Further select features using FCBF
    X_fss = feature_selection_fcbf(X_fs, y)

    return X_fss


