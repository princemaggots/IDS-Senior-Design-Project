import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def read_dataset(filepath):
    df = pd.read_csv(filepath)
    print(df.Label.value_counts())  # Display the distribution of the 'Label' column
    return df

def min_max(df):
    numeric_features = df.select_dtypes(include=[np.number]).columns
    df[numeric_features] = (df[numeric_features] - df[numeric_features].min()) / (df[numeric_features].max() - df[numeric_features].min())
    df.fillna(0, inplace=True)
    return df

def split_train(test_size=0.2, filepath='./data/CICIDS2017_sample.csv'):
    df = read_dataset(filepath)
    df = min_max(df)
    labelencoder = LabelEncoder()
    train_size = 1 - test_size
    df['Label'] = labelencoder.fit_transform(df['Label'])
    X = df.drop(['Label'], axis=1).values
    y = df['Label'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, test_size=test_size, stratify=y)
    return df, X_train, X_test, y_train, y_test

def oversampling_by_SMOTE(X_train, y_train):
    smote = SMOTE(n_jobs=-1, sampling_strategy={4: 1500})
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    print(pd.Series(y_train_res).value_counts())  # Optional: To display the value counts after oversampling
    return X_train_res, y_train_res