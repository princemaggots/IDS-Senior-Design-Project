import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, DecisionTreeClassifier
import xgboost as xgb
from imblearn.over_sampling import SMOTE


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def calculate_feature_importance(dt, rf, et, xg, df):
    """
    Calculates the average feature importance from decision tree, random forest,
    extra trees, and XGBoost models.
    """
    dt_feature = dt.feature_importances_
    rf_feature = rf.feature_importances_
    et_feature = et.feature_importances_
    xgb_feature = xg.feature_importances_
    
    avg_feature = (dt_feature + rf_feature + et_feature + xgb_feature) / 4
    feature_names = (df.drop(['Label'], axis=1)).columns.values
    feature_importance = sorted(zip(map(lambda x: round(x, 4), avg_feature), feature_names), reverse=True)
    
    print("Features sorted by their score:")
    for score, name in feature_importance:
        print(f"{name}: {score}")

    return feature_importance

def select_important_features(feature_importance, df, threshold=0.9):
    """
    Selects important features based on their cumulative importance.
    """
    sum_importance = 0
    selected_features = []
    for importance, feature_name in feature_importance:
        sum_importance += importance
        selected_features.append(feature_name)
        if sum_importance >= threshold:
            break
    
    X_fs = df[selected_features].values
    return X_fs, selected_features

def split_dataset(X, y):
    """
    Splits the dataset into training and test sets.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0, stratify=y)
    return X_train, X_test, y_train, y_test