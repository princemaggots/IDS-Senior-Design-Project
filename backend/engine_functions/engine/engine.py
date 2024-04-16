# import model_trainingLCCDE, model_predictionLCCDE, data_preprocessingLCCDE

from engine_functions.engine.model_predictionLCCDE import LCCDE
from engine_functions.engine.model_trainingLCCDE import train_lightgbm, train_xgboost, train_catboost
from engine_functions.engine.data_preprocessingLCCDE import split_data, apply_smote

def runLCCDE(dataset, test_size, random_state, sampling_strat2, sampling_strat4, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators, cb_iterations, cb_learning_rate, cb_depth, cb_random_state, cb_loss_function, lg_boosting, lg_learning_rate, lg_lambda_l1, lg_num_leaves, lg_num_iterations,lg_max_depth):
    X_train, X_test, y_train, y_test = split_data(dataset=dataset, test_size=test_size, random_state=random_state)
    X_train, y_train = apply_smote(X_train, y_train, sampling_strat2=sampling_strat2, sampling_strat4=sampling_strat4)
    lg, lg_class_f1, lg_class_report, lg_acc_score, lg_prec_score, lg_rec_score, lg_f1, lg_confusion_matrix = train_lightgbm(X_train, y_train, X_test, y_test, lg_boosting, lg_learning_rate, lg_lambda_l1, lg_num_leaves, lg_num_iterations,lg_max_depth)
    xg, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_confusion_matrix = train_xgboost(X_train, y_train, X_test, y_test, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators)
    cb, cb_class_f1, cb_class_report, cb_acc_score, cb_prec_score, cb_rec_score, cb_f1, cb_confusion_matrix = train_catboost(X_train, y_train, X_test, y_test, cb_iterations, cb_learning_rate, cb_depth, cb_random_state, cb_loss_function)

    # Leading model list for each class
    model=[]
    for i in range(len(lg_class_f1)):
        if max(lg_class_f1[i],xg_class_f1[i],cb_class_f1[i]) == lg_class_f1[i]:
            model.append(lg)
        elif max(lg_class_f1[i],xg_class_f1[i],cb_class_f1[i]) == xg_class_f1[i]:
            model.append(xg)
        else:
            model.append(cb)
    
    stack_accuracy, stack_precision, stack_recall, stack_f1, stack_class_f1 = LCCDE(X_test, y_test, m1 = lg, m2 = xg, m3 = cb, model=model)

     # Comparison: The F1-scores for each base model
    print("F1 of LightGBM for each type of attack: "+ str(lg_class_f1))
    print("F1 of XGBoost for each type of attack: "+ str(xg_class_f1))
    print("F1 of CatBoost for each type of attack: "+ str(cb_class_f1))

    return lg_class_f1, lg_class_report, lg_acc_score, lg_prec_score, lg_rec_score, lg_f1, lg_confusion_matrix, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_confusion_matrix, cb_class_f1, cb_class_report, cb_acc_score, cb_prec_score, cb_rec_score, cb_f1, cb_confusion_matrix, stack_accuracy, stack_precision, stack_recall, stack_f1, stack_class_f1

