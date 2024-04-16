
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, DecisionTreeClassifier
import xgboost as xgb
from xgboost import plot_importance
from imblearn.over_sampling import SMOTE

def read_dataset(filepath='./data/CICIDS2017.csv'):
    df = pd.read_csv(filepath)
    print(df.Label.value_counts())  # Display the distribution of the 'Label' column
    return df

def data_sample(df):
    df_minor = df[(df['Label'] == 'WebAttack') | (df['Label'] == 'Bot') | (df['Label'] == 'Infiltration')]
    df_BENIGN = df[df['Label'] == 'BENIGN'].sample(frac=0.01, random_state=42)
    df_DoS = df[df['Label'] == 'DoS'].sample(frac=0.05, random_state=42)
    df_PortScan = df[df['Label'] == 'PortScan'].sample(frac=0.05, random_state=42)
    df_BruteForce = df[df['Label'] == 'BruteForce'].sample(frac=0.2, random_state=42)

    df_s = pd.concat([df_BENIGN, df_DoS, df_PortScan, df_BruteForce, df_minor]).sort_index()
    return df_s

def min_max(df):
    numeric_features = df.select_dtypes(include=[np.number]).columns
    df[numeric_features] = (df[numeric_features] - df[numeric_features].min()) / (df[numeric_features].max() - df[numeric_features].min())
    df.fillna(0, inplace=True)
    return df

def split_train(df):
    labelencoder = LabelEncoder()
    df['Label'] = labelencoder.fit_transform(df['Label'])
    X = df.drop(['Label'], axis=1).values
    y = df['Label'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42, stratify=y)
    return X_train, X_test, y_train, y_test

def oversampling_by_SMOTE(X_train, y_train):
    smote = SMOTE(n_jobs=-1, sampling_strategy={4: 1500})
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    print(pd.Series(y_train_res).value_counts())  # Optional: To display the value counts after oversampling
    return X_train_res, y_train_res