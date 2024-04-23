import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb

def train_decision_tree(X_train, y_train, X_test, y_test, dt_criterion, dt_splitter, dt_max_depth, dt_min_samples_split, dt_min_samples_leaf, dt_min_weight_fraction_leaf, dt_max_features, dt_random_state, dt_max_leaf_nodes):
    print("IUBDYELVBF")
    print(dt_max_depth)
    print(type(dt_max_depth))
    # Function to train and evaluate a decision tree model 
    dt = DecisionTreeClassifier(criterion=dt_criterion, splitter=dt_splitter, max_depth=dt_max_depth, min_samples_split=dt_min_samples_split, min_samples_leaf=dt_min_samples_leaf, min_weight_fraction_leaf=dt_min_weight_fraction_leaf, max_features=dt_max_features, random_state=dt_random_state, max_leaf_nodes=dt_max_leaf_nodes)
    dt.fit(X_train, y_train)
    dt_score = dt.score(X_test, y_test)
    y_pred = dt.predict(X_test)
    dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat = print_evaluation_scores(y_test, y_pred, 'Decision Tree')
    return dt, dt.predict(X_train), dt.predict(X_test), dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat


def train_random_forest(X_train, y_train, X_test, y_test, rf_n_estimators, rf_criterion, rf_max_depth, rf_min_samples_split, rf_min_samples_leaf, rf_min_weight_fractions_leaf, rf_max_features, rf_max_leaf_nodes, rf_random_state):
    # Function to train and evaluate a random forest model
    print("IUBDYELVBF")
    print(rf_max_depth)
    print(type(rf_max_depth))
    rf = RandomForestClassifier(n_estimators = rf_n_estimators, criterion = rf_criterion, max_depth = rf_max_depth, min_samples_split = rf_min_samples_split, min_samples_leaf = rf_min_samples_leaf, min_weight_fraction_leaf = rf_min_weight_fractions_leaf, max_features = rf_max_features, max_leaf_nodes = rf_max_leaf_nodes, random_state=rf_random_state)
    rf.fit(X_train, y_train)
    rf_score = rf.score(X_test, y_test)
    y_pred = rf.predict(X_test)
    rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat = print_evaluation_scores(y_test, y_pred, 'Random Forest')
    print("given accuracy score: ", rf_acc_score)
    print("unnamed accuracy score: ", rf_score)
    return rf, rf.predict(X_train), rf.predict(X_test), rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat

def train_extra_trees(X_train, y_train, X_test, y_test, et_n_estimators, et_criterion, et_max_depth, et_min_samples_split, et_min_samples_leaf, et_min_weight_fractions_leaf, et_max_features, et_max_leaf_nodes, et_random_state):
    # Function to train and evaluate an extra trees model
    et = ExtraTreesClassifier(n_estimators = et_n_estimators, criterion = et_criterion, max_depth = et_max_depth, min_samples_split = et_min_samples_split, min_samples_leaf = et_min_samples_leaf, min_weight_fraction_leaf = et_min_weight_fractions_leaf, max_features = et_max_features, max_leaf_nodes = et_max_leaf_nodes, random_state = et_random_state)
    et.fit(X_train, y_train)
    et_score = et.score(X_test, y_test)
    y_pred = et.predict(X_test)
    et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat = print_evaluation_scores(y_test, y_pred, 'Extra Trees')
    return et, et.predict(X_train), et.predict(X_test), et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat

def train_xgboost(X_train, y_train, X_test, y_test, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators):
    # Function to train and evaluate an XGBoost model
    xg = xgb.XGBClassifier(eta=xg_eta, max_depth=xg_max_depth, subsample=xg_subsample, alpha=xg_alpha, gamma=xg_gamma, colsample_bytree=xg_colsample_bytree, min_child_weight=xg_min_child_weight, n_estimators=xg_n_estimators, reg_lambda=xg_lambda)
    xg.fit(X_train, y_train)
    xg_score = xg.score(X_test, y_test)
    y_pred = xg.predict(X_test)
    xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat = print_evaluation_scores(y_test, y_pred, 'XGBoost')
    return xg, xg.predict(X_train), xg.predict(X_test), xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat

def construct_stacking_model(dt_train, rf_train, et_train, xg_train, dt_test, rf_test, et_test, xg_test, y_train, y_test):
    # Function to construct and evaluate the stacking model
    x_train = np.column_stack((dt_train, rf_train, et_train, xg_train))
    x_test = np.column_stack((dt_test, rf_test, et_test, xg_test))
    stk = xgb.XGBClassifier().fit(x_train, y_train)
    y_pred = stk.predict(x_test)
    class_f1, class_report, acc_score, prec_score, rec_score, f1, conf_mat = print_evaluation_scores(y_test, y_pred, 'Stacking Model')
    return class_f1, class_report, acc_score, prec_score, rec_score, f1, conf_mat

def print_evaluation_scores(y_test, y_pred, model_name):
    # # Helper function to print evaluation scores
    # print(f'Accuracy of {model_name}: {accuracy_score(y_true, y_pred)}')
    # precision, recall, fscore, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')
    # print(f'Precision of {model_name}: {precision}')
    # print(f'Recall of {model_name}: {recall}')
    # print(f'F1-score of {model_name}: {fscore}')
    # print(classification_report(y_true, y_pred))
    # cm = confusion_matrix(y_true, y_pred)
    # Print accuracy, precision, recall, and F1 scores
    class_report = classification_report(y_test, y_pred)
    acc_score = accuracy_score(y_test, y_pred)
    prec_score = precision_score(y_test, y_pred, average='weighted')
    rec_score = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    class_f1 = f1_score(y_test, y_pred, average=None)

    # UNSURE IF PRINTING NECCESSARY
    print(class_report)
    print(f"Accuracy of {model_name}: " + str(acc_score))
    print(f"Precision of {model_name}: " + str(prec_score))
    print(f"Recall of {model_name}: " + str(rec_score))
    print(f"Average F1 of {model_name}: " + str(f1))
    print(f"F1 of {model_name} for each type of attack: " + str(class_f1))
    # UNSURE IF PRINTING NECCESSARY

    # Plot the confusion matrix
    conf_mat = confusion_matrix(y_test, y_pred)
    return class_f1, class_report, acc_score, prec_score, rec_score, f1, conf_mat
