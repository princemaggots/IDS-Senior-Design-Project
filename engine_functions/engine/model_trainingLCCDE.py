import lightgbm as lgb
import xgboost as xgb
import catboost as cbt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

def train_and_evaluate(model, X_train, y_train, X_test, y_test, model_name):

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

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
    confusion_matrix = plot_confusion_matrix(y_test, y_pred)
    return class_f1, class_report, acc_score, prec_score, rec_score, f1, confusion_matrix

def plot_confusion_matrix(y_true, y_pred):
    cf = confusion_matrix(y_true, y_pred)
    # f, ax = plt.subplots(figsize=(5,5))
    # sns.heatmap(cf, annot=True, linewidth=0.5, linecolor="red", fmt=".0f", ax=ax)
    # plt.xlabel("Predicted")
    # plt.ylabel("Actual")
    return cf

def select_leading_models(lg_f1, xg_f1, cb_f1, models):
    leading_models = []
    for i in range(len(lg_f1)):
        max_f1 = max(lg_f1[i], xg_f1[i], cb_f1[i])
        if max_f1 == lg_f1[i]:
            leading_models.append(models['lg'])
        elif max_f1 == xg_f1[i]:
            leading_models.append(models['xg'])
        else:
            leading_models.append(models['cb'])
    return leading_models

def train_lightgbm(X_train, y_train, X_test, y_test, lg_boosting, lg_learning_rate, lg_lambda_l1, lg_num_leaves, lg_num_iterations,lg_max_depth):
    lg = lgb.LGBMClassifier(boosting=lg_boosting, learning_rate=lg_learning_rate, lambda_l1=lg_lambda_l1, num_leaves=lg_num_leaves, num_iterations=lg_num_iterations, max_depth=lg_max_depth)
    class_f1, class_report, acc_score, prec_score, rec_score, f1, confusion_matrix = train_and_evaluate(lg, X_train, y_train, X_test, y_test, 'LightGBM')
    return lg, class_f1, class_report, acc_score, prec_score, rec_score, f1, confusion_matrix

def train_xgboost(X_train, y_train, X_test, y_test, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators):
    xg = xgb.XGBClassifier(eta=xg_eta, max_depth=xg_max_depth, subsample=xg_subsample, alpha=xg_alpha, gamma=xg_gamma, colsample_bytree=xg_colsample_bytree, min_child_weight=xg_min_child_weight, n_estimators=xg_n_estimators, reg_lambda=xg_lambda)
    class_f1, class_report, acc_score, prec_score, rec_score, f1, confusion_matrix = train_and_evaluate(xg, X_train, y_train, X_test, y_test, 'XGBoost')
    return xg, class_f1, class_report, acc_score, prec_score, rec_score, f1, confusion_matrix

def train_catboost(X_train, y_train, X_test, y_test, cb_iterations, cb_learning_rate, cb_depth, cb_random_state, cb_loss_function):
    cb = cbt.CatBoostClassifier(verbose=0, boosting_type='Plain', iterations=cb_iterations, learning_rate=cb_learning_rate, depth=cb_depth, random_state=cb_random_state, loss_function=cb_loss_function)
    class_f1, class_report, acc_score, prec_score, rec_score, f1, confusion_matrix = train_and_evaluate(cb, X_train, y_train, X_test, y_test, 'CatBoost')
    return cb, class_f1, class_report, acc_score, prec_score, rec_score, f1, confusion_matrix