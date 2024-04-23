import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from engine_functions.engine.FCBF_module.FCBF_module import FCBFK  # Assuming FCBF module provides the FCBFK class

def calculate_importances(X_train, y_train):
    """Calculate the mutual information of features with respect to the target."""
    importances = mutual_info_classif(X_train, y_train)
    return importances

def select_important_features(importances, features, threshold=0.9):
    """Select features based on their importance scores until the cumulative importance reaches a threshold."""
    total_importance = sum(importances)
    normalized_importances = [importance / total_importance for importance in importances]
    sorted_features = sorted(zip(normalized_importances, features), reverse=True)
    cumulative_importance = 0
    selected_features = []
    for importance, feature in sorted_features:
        cumulative_importance += importance
        selected_features.append(feature)
        if cumulative_importance >= threshold:
            break
    return selected_features

def extract_features(df, selected_features):
    """Extract the selected features from the DataFrame."""
    return df[selected_features].values

def apply_fcbf(X, y, k=20):
    """Apply Fast Correlation Based Filter to reduce feature dimensions."""
    fcbf = FCBFK(k=k)
    X_reduced = fcbf.fit_transform(X, y)
    return X_reduced

def resample_data(X, y):
    """Apply SMOTE to balance the dataset."""
    smote = SMOTE(n_jobs=-1, sampling_strategy={2:1000, 4:1000})
    X_resampled, y_resampled = smote.fit_resample(X, y)
    return X_resampled, y_resampled

def split_data(X, y):
    """Split data into train and test sets."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0, stratify=y)
    return X_train, X_test, y_train, y_test

def main_preprocess(filepath):
    """Main function to preprocess data, select and reduce features, and resample data."""
    df = pd.read_csv(filepath)
    X_train = df.drop(['Label'], axis=1).values
    y_train = df['Label'].values
    features = df.drop(['Label'], axis=1).columns.tolist()

    importances = calculate_importances(X_train, y_train)
    selected_features = select_important_features(importances, features)
    X_fs = extract_features(df, selected_features)

    X_fss = apply_fcbf(X_fs, y_train)
    X_train, X_test, y_train, y_test = split_data(X_fss, y_train)
    X_train, y_train = resample_data(X_train, y_train)

    return X_train, X_test, y_train, y_test