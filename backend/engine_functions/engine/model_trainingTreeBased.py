
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

def train_decision_tree(X_train, y_train, X_test, y_test):
    # Function to train and evaluate a decision tree model 
    dt = DecisionTreeClassifier(random_state=0)
    dt.fit(X_train, y_train)
    dt_score = dt.score(X_test, y_test)
    y_pred = dt.predict(X_test)
    print_evaluation_scores(y_test, y_pred, 'Decision Tree')
    return dt.predict(X_train), dt.predict(X_test), dt_score


def train_random_forest(X_train, y_train, X_test, y_test):
    # Function to train and evaluate a random forest model
    rf = RandomForestClassifier(random_state=0)
    rf.fit(X_train, y_train)
    rf_score = rf.score(X_test, y_test)
    y_pred = rf.predict(X_test)
    print_evaluation_scores(y_test, y_pred, 'Random Forest')
    return rf.predict(X_train), rf.predict(X_test), rf_score

def train_extra_trees(X_train, y_train, X_test, y_test):
    # Function to train and evaluate an extra trees model
    et = ExtraTreesClassifier(random_state=0)
    et.fit(X_train, y_train)
    et_score = et.score(X_test, y_test)
    y_pred = et.predict(X_test)
    print_evaluation_scores(y_test, y_pred, 'Extra Trees')
    return et.predict(X_train), et.predict(X_test), et_score

def train_xgboost(X_train, y_train, X_test, y_test):
    # Function to train and evaluate an XGBoost model
    xg = xgb.XGBClassifier(n_estimators=10)
    xg.fit(X_train, y_train)
    xg_score = xg.score(X_test, y_test)
    y_pred = xg.predict(X_test)
    print_evaluation_scores(y_test, y_pred, 'XGBoost')
    return xg.predict(X_train), xg.predict(X_test), xg_score

def construct_stacking_model(dt_train, rf_train, et_train, xg_train, dt_test, rf_test, et_test, xg_test, y_train, y_test):
    # Function to construct and evaluate the stacking model
    x_train = np.column_stack((dt_train, rf_train, et_train, xg_train))
    x_test = np.column_stack((dt_test, rf_test, et_test, xg_test))
    stk = xgb.XGBClassifier().fit(x_train, y_train)
    y_pred = stk.predict(x_test)
    print_evaluation_scores(y_test, y_pred, 'Stacking Model')

def print_evaluation_scores(y_true, y_pred, model_name):
    # Helper function to print evaluation scores
    print(f'Accuracy of {model_name}: {accuracy_score(y_true, y_pred)}')
    precision, recall, fscore, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')
    print(f'Precision of {model_name}: {precision}')
    print(f'Recall of {model_name}: {recall}')
    print(f'F1-score of {model_name}: {fscore}')
    print(classification_report(y_true, y_pred))
    cm = confusion_matrix(y_true, y_pred)
    f, ax = plt.subplots(figsize=(5, 5))
    sns.heatmap(cm, annot=True, linewidth=0.5, linecolor="red", fmt=".0f", ax=ax)
    plt.xlabel("y_pred")
    plt.ylabel("y_true")
    plt.show()