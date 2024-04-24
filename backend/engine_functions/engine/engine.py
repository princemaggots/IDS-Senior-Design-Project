# import model_trainingLCCDE, model_predictionLCCDE, data_preprocessingLCCDE

from engine_functions.engine.model_predictionLCCDE import LCCDE
from engine_functions.engine.model_trainingLCCDE import train_lightgbm, train_xgboost_lccde, train_catboost
from engine_functions.engine.data_preprocessingLCCDE import split_data, apply_smote

from engine_functions.engine.pre_processingTreeBased import split_train, oversampling_by_SMOTE
from engine_functions.engine.model_trainingTreeBased import train_decision_tree, train_extra_trees, train_random_forest, train_xgboost, construct_stacking_model
from engine_functions.engine.feature_selectionTreeBased import calculate_feature_importance, select_important_features, split_dataset

# from engine_functions.engine.date_preprocessingMTH import preprocess_data
from engine_functions.engine.feature_selectionMTH import main_preprocess

def runLCCDE(dataset, test_size, random_state, sampling_strat2, sampling_strat4, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators, cb_iterations, cb_learning_rate, cb_depth, cb_random_state, cb_loss_function, lg_boosting, lg_learning_rate, lg_lambda_l1, lg_num_leaves, lg_num_iterations,lg_max_depth):
    X_train, X_test, y_train, y_test = split_data(dataset=dataset, test_size=test_size, random_state=random_state)
    X_train, y_train = apply_smote(X_train, y_train, sampling_strat2=sampling_strat2, sampling_strat4=sampling_strat4)
    lg, lg_class_f1, lg_class_report, lg_acc_score, lg_prec_score, lg_rec_score, lg_f1, lg_confusion_matrix = train_lightgbm(X_train, y_train, X_test, y_test, lg_boosting, lg_learning_rate, lg_lambda_l1, lg_num_leaves, lg_num_iterations,lg_max_depth)
    xg, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_confusion_matrix = train_xgboost_lccde(X_train, y_train, X_test, y_test, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators)
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


def runMTH(test_size, dataset, feature_selection_threshold, fcbf_k, dt_criterion, dt_splitter, dt_max_depth, dt_min_samples_split, dt_min_samples_leaf, dt_min_weight_fraction_leaf, dt_max_features, dt_random_state, dt_max_leaf_nodes, rf_n_estimators, rf_criterion, rf_max_depth, rf_min_samples_split, rf_min_samples_leaf, rf_min_weight_fractions_leaf, rf_max_features, rf_max_leaf_nodes, rf_random_state, et_n_estimators, et_criterion, et_max_depth, et_min_samples_split, et_min_samples_leaf, et_min_weight_fractions_leaf, et_max_features, et_max_leaf_nodes, et_random_state, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators):
    if dataset == "CICIDS2017":
        filepath = "./engine_functions/engine/data/CICIDS2017_sample_km.csv"
    else:
        filepath = "./engine_functions/engine/data/CICIDS2017_sample_km.csv"
        
    X_train, X_test, y_train, y_test = main_preprocess(filepath)

    if dt_max_depth == "0":
        dt_max_depth = None

    if dt_max_leaf_nodes == "0":
        dt_max_leaf_nodes = None

    if et_max_depth == "0":
        et_max_depth = None

    if et_max_leaf_nodes == "0":
        et_max_leaf_nodes = None
    
    if rf_max_depth == "0":
        rf_max_depth = None

    if rf_max_leaf_nodes == "0":
        rf_max_leaf_nodes = None


    if dt_max_features == "sqrt":
        pass
    elif dt_max_features == "log2":
        pass
    elif dt_max_features == "0":
        dt_max_features = None
    else:
        dt_max_features = float(dt_max_features)

    if et_max_features == "sqrt":
        pass
    elif et_max_features == "log2":
        pass
    elif et_max_features == "0":
        et_max_features = None
    else:
        et_max_features = float(et_max_features)
    
    if rf_max_features == "sqrt":
        pass
    elif rf_max_features == "log2":
        pass
    elif rf_max_features == "0":
        rf_max_features = None
    else:
        rf_max_features = float(rf_max_features)
    
    dt_min_samples_split = float(dt_min_samples_split) if "." in str(dt_min_samples_split) else int(dt_min_samples_split)
    dt_min_samples_leaf = float(dt_min_samples_leaf) if "." in str(dt_min_samples_leaf) else int(dt_min_samples_leaf)
    et_min_samples_split = float(et_min_samples_split) if "." in str(et_min_samples_split) else int(et_min_samples_split)
    et_min_samples_leaf = float(et_min_samples_leaf) if "." in str(et_min_samples_leaf) else int(et_min_samples_leaf)
    rf_min_samples_split = float(rf_min_samples_split) if "." in str(rf_min_samples_split) else int(rf_min_samples_split)
    rf_min_samples_leaf = float(rf_min_samples_leaf) if "." in str(rf_min_samples_leaf) else int(rf_min_samples_leaf)

    dt, dt_predict_X_train, dt_predict_X_test, dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat = train_decision_tree(X_train, y_train, X_test, y_test, dt_criterion, dt_splitter, dt_max_depth, dt_min_samples_split, dt_min_samples_leaf, dt_min_weight_fraction_leaf, dt_max_features, dt_random_state, dt_max_leaf_nodes)
    rf, rf_predict_X_train, rf_predict_X_test, rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat = train_random_forest(X_train, y_train, X_test, y_test, rf_n_estimators, rf_criterion, rf_max_depth, rf_min_samples_split, rf_min_samples_leaf, rf_min_weight_fractions_leaf, rf_max_features, rf_max_leaf_nodes, rf_random_state)
    et, et_predict_X_train, et_predict_X_test, et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat = train_extra_trees(X_train, y_train, X_test, y_test, et_n_estimators, et_criterion, et_max_depth, et_min_samples_split, et_min_samples_leaf, et_min_weight_fractions_leaf, et_max_features, et_max_leaf_nodes, et_random_state)
    xg, xg_predict_X_train, xg_predict_X_test, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat = train_xgboost(X_train, y_train, X_test, y_test, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators)
    stack_class_f1, stack_class_report, stack_acc_score, stack_prec_score, stack_rec_score, stack_f1, stack_conf_mat = construct_stacking_model(dt_predict_X_train, rf_predict_X_train, et_predict_X_train, xg_predict_X_train, dt_predict_X_test, rf_predict_X_test, et_predict_X_test, xg_predict_X_test, y_train, y_test)

    return dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat, rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat, et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat, stack_class_f1, stack_class_report, stack_acc_score, stack_prec_score, stack_rec_score, stack_f1, stack_conf_mat



def runTreeBased(test_size, feature_selection, dataset, feature_selection_threshold, dt_criterion, dt_splitter, dt_max_depth, dt_min_samples_split, dt_min_samples_leaf, dt_min_weight_fraction_leaf, dt_max_features, dt_random_state, dt_max_leaf_nodes, rf_n_estimators, rf_criterion, rf_max_depth, rf_min_samples_split, rf_min_samples_leaf, rf_min_weight_fractions_leaf, rf_max_features, rf_max_leaf_nodes, rf_random_state, et_n_estimators, et_criterion, et_max_depth, et_min_samples_split, et_min_samples_leaf, et_min_weight_fractions_leaf, et_max_features, et_max_leaf_nodes, et_random_state, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators):

    # clarify some params
    
    if dataset == "CICIDS2017":
        filepath = "./engine_functions/engine/data/CICIDS2017_sample_km.csv"
    else:
        filepath = "./engine_functions/engine/data/CICIDS2017_sample_km.csv"
    
    if feature_selection == 0:
        feature_selection = False
    else:
        feature_selection = True

    if dt_max_depth == "0":
        dt_max_depth = None

    if dt_max_leaf_nodes == "0":
        dt_max_leaf_nodes = None

    if et_max_depth == "0":
        et_max_depth = None

    if et_max_leaf_nodes == "0":
        et_max_leaf_nodes = None
    
    if rf_max_depth == "0":
        rf_max_depth = None

    if rf_max_leaf_nodes == "0":
        rf_max_leaf_nodes = None


    if dt_max_features == "sqrt":
        pass
    elif dt_max_features == "log2":
        pass
    elif dt_max_features == "0":
        dt_max_features = None
    else:
        dt_max_features = float(dt_max_features)

    if et_max_features == "sqrt":
        pass
    elif et_max_features == "log2":
        pass
    elif et_max_features == "0":
        et_max_features = None
    else:
        et_max_features = float(et_max_features)
    
    if rf_max_features == "sqrt":
        pass
    elif rf_max_features == "log2":
        pass
    elif rf_max_features == "0":
        rf_max_features = None
    else:
        rf_max_features = float(rf_max_features)
    
    dt_min_samples_split = float(dt_min_samples_split) if "." in str(dt_min_samples_split) else int(dt_min_samples_split)
    dt_min_samples_leaf = float(dt_min_samples_leaf) if "." in str(dt_min_samples_leaf) else int(dt_min_samples_leaf)
    et_min_samples_split = float(et_min_samples_split) if "." in str(et_min_samples_split) else int(et_min_samples_split)
    et_min_samples_leaf = float(et_min_samples_leaf) if "." in str(et_min_samples_leaf) else int(et_min_samples_leaf)
    rf_min_samples_split = float(rf_min_samples_split) if "." in str(rf_min_samples_split) else int(rf_min_samples_split)
    rf_min_samples_leaf = float(rf_min_samples_leaf) if "." in str(rf_min_samples_leaf) else int(rf_min_samples_leaf)


    df, X_train, X_test, y_train, y_test = split_train(filepath=filepath, test_size=test_size)
    X_train, y_train = oversampling_by_SMOTE(X_train, y_train)

    # run once

    dt, dt_predict_X_train, dt_predict_X_test, dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat = train_decision_tree(X_train, y_train, X_test, y_test, dt_criterion, dt_splitter, dt_max_depth, dt_min_samples_split, dt_min_samples_leaf, dt_min_weight_fraction_leaf, dt_max_features, dt_random_state, dt_max_leaf_nodes)
    rf, rf_predict_X_train, rf_predict_X_test, rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat = train_random_forest(X_train, y_train, X_test, y_test, rf_n_estimators, rf_criterion, rf_max_depth, rf_min_samples_split, rf_min_samples_leaf, rf_min_weight_fractions_leaf, rf_max_features, rf_max_leaf_nodes, rf_random_state)
    et, et_predict_X_train, et_predict_X_test, et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat = train_extra_trees(X_train, y_train, X_test, y_test, et_n_estimators, et_criterion, et_max_depth, et_min_samples_split, et_min_samples_leaf, et_min_weight_fractions_leaf, et_max_features, et_max_leaf_nodes, et_random_state)
    xg, xg_predict_X_train, xg_predict_X_test, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat = train_xgboost(X_train, y_train, X_test, y_test, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators)
    stack_class_f1, stack_class_report, stack_acc_score, stack_prec_score, stack_rec_score, stack_f1, stack_conf_mat = construct_stacking_model(dt_predict_X_train, rf_predict_X_train, et_predict_X_train, xg_predict_X_train, dt_predict_X_test, rf_predict_X_test, et_predict_X_test, xg_predict_X_test, y_train, y_test)

    # feature selection
    if (feature_selection):
        feature_importance = calculate_feature_importance(dt, rf, et, xg, df)
        X_fs, selected_features = select_important_features(feature_importance, df, threshold=feature_selection_threshold)
        X_train, X_test, y_train, y_test = split_dataset(X_fs,df['Label'].values,test_size)
        # run again :(
        dt, dt_predict_X_train, dt_predict_X_test, dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat = train_decision_tree(X_train, y_train, X_test, y_test, dt_criterion, dt_splitter, dt_max_depth, dt_min_samples_split, dt_min_samples_leaf, dt_min_weight_fraction_leaf, dt_max_features, dt_random_state, dt_max_leaf_nodes)
        rf, rf_predict_X_train, rf_predict_X_test, rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat = train_random_forest(X_train, y_train, X_test, y_test, rf_n_estimators, rf_criterion, rf_max_depth, rf_min_samples_split, rf_min_samples_leaf, rf_min_weight_fractions_leaf, rf_max_features, rf_max_leaf_nodes, rf_random_state)
        et, et_predict_X_train, et_predict_X_test, et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat = train_extra_trees(X_train, y_train, X_test, y_test, et_n_estimators, et_criterion, et_max_depth, et_min_samples_split, et_min_samples_leaf, et_min_weight_fractions_leaf, et_max_features, et_max_leaf_nodes, et_random_state)
        xg, xg_predict_X_train, xg_predict_X_test, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat = train_xgboost(X_train, y_train, X_test, y_test, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators)
        stack_class_f1, stack_class_report, stack_acc_score, stack_prec_score, stack_rec_score, stack_f1, stack_conf_mat = construct_stacking_model(dt_predict_X_train, rf_predict_X_train, et_predict_X_train, xg_predict_X_train, dt_predict_X_test, rf_predict_X_test, et_predict_X_test, xg_predict_X_test, y_train, y_test)

    
    return dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat, rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat, et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat, stack_class_f1, stack_class_report, stack_acc_score, stack_prec_score, stack_rec_score, stack_f1, stack_conf_mat








