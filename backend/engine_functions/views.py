from django.http import HttpResponse, JsonResponse
from engine_functions.engine.engine import runLCCDE, runTreeBased, runMTH
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json

@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the engine_functions index!")

@csrf_exempt
def lccde_run(request):
    data = json.loads(request.body)
    print(data)
    dataset = data.get('dataset')
    test_size = float(data.get('test_size'))
    random_state = int(data.get('random_state'))
    sampling_strat2 = int(data.get('sampling_strat2'))
    sampling_strat4 = int(data.get('sampling_strat4'))
    xg_eta = float(data.get('xg_eta'))
    xg_max_depth = int(data.get('xg_max_depth'))
    xg_subsample = float(data.get('xg_subsample'))
    xg_lambda = int(data.get('xg_lambda'))
    xg_alpha = int(data.get('xg_alpha'))
    xg_gamma = int(data.get('xg_gamma'))
    xg_colsample_bytree = float(data.get('xg_colsample_bytree'))
    xg_min_child_weight = int(data.get('xg_min_child_weight'))
    xg_n_estimators = int(data.get('xg_n_estimators'))
    cb_iterations = int(data.get('cb_iterations'))
    cb_learning_rate = float(data.get('cb_learning_rate'))
    cb_depth = int(data.get('cb_depth', 6))
    cb_random_state = int(data.get('cb_random_state'))
    cb_loss_function = data.get('cb_loss_function')
    lg_boosting = data.get('lg_boosting')
    lg_learning_rate = float(data.get('lg_learning_rate'))
    lg_lambda_l1 = float(data.get('lg_lambda_l1'))
    lg_num_leaves = int(data.get('lg_num_leaves'))
    lg_num_iterations = int(data.get('lg_num_iterations'))
    lg_max_depth = int(data.get('lg_max_depth'))

    time_A = datetime.now()


 # dataset="CICIDS2017", test_size=0.2, random_state=0, sampling_strat2=1000, sampling_strat4=1000

    lg_class_f1, lg_class_report, lg_acc_score, lg_prec_score, lg_rec_score, lg_f1, lg_confusion_matrix, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_confusion_matrix, cb_class_f1, cb_class_report, cb_acc_score, cb_prec_score, cb_rec_score, cb_f1, cb_confusion_matrix, stack_accuracy, stack_precision, stack_recall, stack_f1, stack_class_f1 = runLCCDE(dataset=dataset, test_size=test_size, random_state=random_state, sampling_strat2=sampling_strat2, sampling_strat4=sampling_strat4, xg_eta=xg_eta, xg_max_depth=xg_max_depth, xg_subsample=xg_subsample, xg_lambda=xg_lambda, xg_alpha=xg_alpha, xg_gamma=xg_gamma, xg_colsample_bytree=xg_colsample_bytree, xg_min_child_weight=xg_min_child_weight, xg_n_estimators=xg_n_estimators, cb_iterations=cb_iterations, cb_learning_rate=cb_learning_rate, cb_depth=cb_depth, cb_random_state=cb_random_state, cb_loss_function=cb_loss_function, lg_boosting=lg_boosting, lg_learning_rate=lg_learning_rate, lg_lambda_l1=lg_lambda_l1, lg_num_leaves=lg_num_leaves, lg_num_iterations=lg_num_iterations,lg_max_depth=lg_max_depth)

    lg_class_f1 = lg_class_f1.tolist()
    xg_class_f1 = xg_class_f1.tolist()
    cb_class_f1 = cb_class_f1.tolist()
    stack_class_f1 = stack_class_f1.tolist()
    lg_confusion_matrix = lg_confusion_matrix.tolist()
    xg_confusion_matrix = xg_confusion_matrix.tolist()
    cb_confusion_matrix = cb_confusion_matrix.tolist()

    time_B = datetime.now()

    elapsed_time = time_B - time_A

    data = {
        'lg_class_f1': lg_class_f1,
        'lg_class_report': lg_class_report,
        'lg_acc_score': lg_acc_score,
        'lg_prec_score': lg_prec_score,
        'lg_rec_score': lg_rec_score,
        'lg_f1': lg_f1,
        'lg_confusion_matrix': lg_confusion_matrix,

        'xb_class_f1': xg_class_f1,
        'xb_class_report': xg_class_report,
        'xb_acc_score': xg_acc_score,
        'xb_prec_score': xg_prec_score,
        'xb_rec_score': xg_rec_score,
        'xb_f1': xg_f1,
        'xb_confusion_matrix': xg_confusion_matrix,

        'cb_class_f1': cb_class_f1,
        'cb_class_report': cb_class_report,
        'cb_acc_score': cb_acc_score,
        'cb_prec_score': cb_prec_score,
        'cb_rec_score': cb_rec_score,
        'cb_f1': cb_f1,
        'cb_confusion_matrix': cb_confusion_matrix,

        'stack_class_f1': stack_class_f1,
        'stack_acc_score': stack_accuracy,
        'stack_prec_score': stack_precision,
        'stack_rec_score': stack_recall,
        'stack_f1': stack_f1,

        'runtime' : elapsed_time.seconds
    }

    return JsonResponse(data)

    # return HttpResponse("I mean, I think it ran")

@csrf_exempt
def mth_run(request):
    data = json.loads(request.body)
    print(data)
    dataset = data.get('dataset')
    fcbf_k = data.get('fcbf_k')
    test_size = float(data.get('test_size'))
    feature_selection_threshold = float(data.get('feature_selection_threshold'))
    dt_criterion = data.get('dt_criterion')
    dt_splitter = data.get('dt_splitter')
    dt_max_depth = data.get('dt_max_depth')
    dt_min_samples_split = data.get('dt_min_samples_split')
    dt_min_samples_leaf = data.get('dt_min_samples_leaf')
    dt_min_weight_fraction_leaf = float(data.get('dt_min_weight_fraction_leaf'))
    dt_max_features = data.get('dt_max_features')
    dt_random_state = int(data.get('dt_random_state'))
    dt_max_leaf_nodes = data.get('dt_max_leaf_nodes')
    xg_eta = float(data.get('xg_eta'))
    xg_max_depth = data.get('xg_max_depth')
    xg_subsample = float(data.get('xg_subsample'))
    xg_lambda = int(data.get('xg_lambda'))
    xg_alpha = int(data.get('xg_alpha'))
    xg_gamma = int(data.get('xg_gamma'))
    xg_colsample_bytree = float(data.get('xg_colsample_bytree'))
    xg_min_child_weight = int(data.get('xg_min_child_weight'))
    xg_n_estimators = int(data.get('xg_n_estimators'))
    rf_n_estimators = int(data.get('rf_n_estimators'))
    rf_criterion = data.get('rf_criterion')
    rf_max_depth = data.get('rf_max_depth')
    rf_min_samples_split = data.get('rf_min_samples_split')
    rf_min_samples_leaf = data.get('rf_min_samples_leaf')
    rf_min_weight_fractions_leaf = float(data.get('rf_min_weight_fractions_leaf'))
    rf_max_features = data.get('rf_max_features')
    rf_max_leaf_nodes = data.get('rf_max_leaf_nodes')
    rf_random_state = int(data.get('rf_random_state'))
    et_n_estimators = int(data.get('et_n_estimators'))
    et_criterion = data.get('et_criterion')
    et_max_depth = data.get('et_max_depth')
    et_min_samples_split = data.get('et_min_samples_split')
    et_min_samples_leaf = data.get('et_min_samples_leaf')
    et_min_weight_fractions_leaf = float(data.get('et_min_weight_fractions_leaf'))
    et_max_features = data.get('et_max_features')
    et_max_leaf_nodes = data.get('et_max_leaf_nodes')
    et_random_state = int(data.get('et_random_state'))

    time_A = datetime.now()

    dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat, rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat, et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat, stack_class_f1, stack_class_report, stack_acc_score, stack_prec_score, stack_rec_score, stack_f1, stack_conf_mat = runMTH(test_size, dataset, feature_selection_threshold, fcbf_k, dt_criterion, dt_splitter, dt_max_depth, dt_min_samples_split, dt_min_samples_leaf, dt_min_weight_fraction_leaf, dt_max_features, dt_random_state, dt_max_leaf_nodes, rf_n_estimators, rf_criterion, rf_max_depth, rf_min_samples_split, rf_min_samples_leaf, rf_min_weight_fractions_leaf, rf_max_features, rf_max_leaf_nodes, rf_random_state, et_n_estimators, et_criterion, et_max_depth, et_min_samples_split, et_min_samples_leaf, et_min_weight_fractions_leaf, et_max_features, et_max_leaf_nodes, et_random_state, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators)

    dt_class_f1 = dt_class_f1.tolist()
    rf_class_f1 = rf_class_f1.tolist()
    et_class_f1 = et_class_f1.tolist()
    xg_class_f1 = xg_class_f1.tolist()
    stack_class_f1 = stack_class_f1.tolist()
    dt_conf_mat = dt_conf_mat.tolist()
    et_conf_mat = et_conf_mat.tolist()
    rf_conf_mat = rf_conf_mat.tolist()
    xg_conf_mat = xg_conf_mat.tolist()

    time_B = datetime.now()
    elapsed_time = time_B - time_A

    data = {
        'dt_class_f1': dt_class_f1,
        'dt_class_report': dt_class_report,
        'dt_acc_score': dt_acc_score,
        'dt_prec_score': dt_prec_score,
        'dt_rec_score': dt_rec_score,
        'dt_f1': dt_f1,
        'dt_confusion_matrix': dt_conf_mat,

        'rf_class_f1': rf_class_f1,
        'rf_class_report': rf_class_report,
        'rf_acc_score': rf_acc_score,
        'rf_prec_score': rf_prec_score,
        'rf_rec_score': rf_rec_score,
        'rf_f1': rf_f1,
        'rf_confusion_matrix': rf_conf_mat,

        'et_class_f1': et_class_f1,
        'et_class_report': et_class_report,
        'et_acc_score': et_acc_score,
        'et_prec_score': et_prec_score,
        'et_rec_score': et_rec_score,
        'et_f1': et_f1,
        'et_confusion_matrix': et_conf_mat,

        'xg_class_f1': xg_class_f1,
        'xg_class_report': xg_class_report,
        'xg_acc_score': xg_acc_score,
        'xg_prec_score': xg_prec_score,
        'xg_rec_score': xg_rec_score,
        'xg_f1': xg_f1,
        'xg_confusion_matrix': xg_conf_mat,

        'stack_class_f1': stack_class_f1,
        'stack_class_report': stack_class_report,
        'stack_acc_score': stack_acc_score,
        'stack_prec_score': stack_prec_score,
        'stack_rec_score': stack_rec_score,
        'stack_f1': stack_f1,

        'runtime' : elapsed_time.seconds
    }

    return JsonResponse(data)

@csrf_exempt
def treebased_run(request):
    data = json.loads(request.body)
    dataset = data.get('dataset')
    test_size = float(data.get('test_size'))
    feature_selection = float(data.get('feature_selection'))
    feature_selection_threshold = float(data.get('feature_selection_threshold'))
    dt_criterion = data.get('dt_criterion')
    dt_splitter = data.get('dt_splitter')
    dt_max_depth = data.get('dt_max_depth')
    dt_min_samples_split = data.get('dt_min_samples_split')
    dt_min_samples_leaf = data.get('dt_min_samples_leaf')
    dt_min_weight_fraction_leaf = float(data.get('dt_min_weight_fraction_leaf'))
    dt_max_features = data.get('dt_max_features')
    dt_random_state = int(data.get('dt_random_state'))
    dt_max_leaf_nodes = data.get('dt_max_leaf_nodes')
    xg_eta = float(data.get('xg_eta'))
    xg_max_depth = data.get('xg_max_depth')
    xg_subsample = float(data.get('xg_subsample'))
    xg_lambda = int(data.get('xg_lambda'))
    xg_alpha = int(data.get('xg_alpha'))
    xg_gamma = int(data.get('xg_gamma'))
    xg_colsample_bytree = float(data.get('xg_colsample_bytree'))
    xg_min_child_weight = int(data.get('xg_min_child_weight'))
    xg_n_estimators = int(data.get('xg_n_estimators'))
    rf_n_estimators = int(data.get('rf_n_estimators'))
    rf_criterion = data.get('rf_criterion')
    rf_max_depth = data.get('rf_max_depth')
    rf_min_samples_split = data.get('rf_min_samples_split')
    rf_min_samples_leaf = data.get('rf_min_samples_leaf')
    rf_min_weight_fractions_leaf = float(data.get('rf_min_weight_fractions_leaf'))
    rf_max_features = data.get('rf_max_features')
    rf_max_leaf_nodes = data.get('rf_max_leaf_nodes')
    rf_random_state = int(data.get('rf_random_state'))
    et_n_estimators = int(data.get('et_n_estimators'))
    et_criterion = data.get('et_criterion')
    et_max_depth = data.get('et_max_depth')
    et_min_samples_split = data.get('et_min_samples_split')
    et_min_samples_leaf = data.get('et_min_samples_leaf')
    et_min_weight_fractions_leaf = float(data.get('et_min_weight_fractions_leaf'))
    et_max_features = data.get('et_max_features')
    et_max_leaf_nodes = data.get('et_max_leaf_nodes')
    et_random_state = int(data.get('et_random_state'))

    time_A = datetime.now()

    dt_class_f1, dt_class_report, dt_acc_score, dt_prec_score, dt_rec_score, dt_f1, dt_conf_mat, rf_class_f1, rf_class_report, rf_acc_score, rf_prec_score, rf_rec_score, rf_f1, rf_conf_mat, et_class_f1, et_class_report, et_acc_score, et_prec_score, et_rec_score, et_f1, et_conf_mat, xg_class_f1, xg_class_report, xg_acc_score, xg_prec_score, xg_rec_score, xg_f1, xg_conf_mat, stack_class_f1, stack_class_report, stack_acc_score, stack_prec_score, stack_rec_score, stack_f1, stack_conf_mat = runTreeBased(test_size, feature_selection, dataset, feature_selection_threshold, dt_criterion, dt_splitter, dt_max_depth, dt_min_samples_split, dt_min_samples_leaf, dt_min_weight_fraction_leaf, dt_max_features, dt_random_state, dt_max_leaf_nodes, rf_n_estimators, rf_criterion, rf_max_depth, rf_min_samples_split, rf_min_samples_leaf, rf_min_weight_fractions_leaf, rf_max_features, rf_max_leaf_nodes, rf_random_state, et_n_estimators, et_criterion, et_max_depth, et_min_samples_split, et_min_samples_leaf, et_min_weight_fractions_leaf, et_max_features, et_max_leaf_nodes, et_random_state, xg_eta, xg_max_depth, xg_subsample, xg_lambda, xg_alpha, xg_gamma, xg_colsample_bytree, xg_min_child_weight, xg_n_estimators)

    dt_class_f1 = dt_class_f1.tolist()
    rf_class_f1 = rf_class_f1.tolist()
    et_class_f1 = et_class_f1.tolist()
    xg_class_f1 = xg_class_f1.tolist()
    stack_class_f1 = stack_class_f1.tolist()
    dt_conf_mat = dt_conf_mat.tolist()
    et_conf_mat = et_conf_mat.tolist()
    rf_conf_mat = rf_conf_mat.tolist()
    xg_conf_mat = xg_conf_mat.tolist()

    time_B = datetime.now()
    elapsed_time = time_B - time_A

    data = {
        'dt_class_f1': dt_class_f1,
        'dt_class_report': dt_class_report,
        'dt_acc_score': dt_acc_score,
        'dt_prec_score': dt_prec_score,
        'dt_rec_score': dt_rec_score,
        'dt_f1': dt_f1,
        'dt_confusion_matrix': dt_conf_mat,

        'rf_class_f1': rf_class_f1,
        'rf_class_report': rf_class_report,
        'rf_acc_score': rf_acc_score,
        'rf_prec_score': rf_prec_score,
        'rf_rec_score': rf_rec_score,
        'rf_f1': rf_f1,
        'rf_confusion_matrix': rf_conf_mat,

        'et_class_f1': et_class_f1,
        'et_class_report': et_class_report,
        'et_acc_score': et_acc_score,
        'et_prec_score': et_prec_score,
        'et_rec_score': et_rec_score,
        'et_f1': et_f1,
        'et_confusion_matrix': et_conf_mat,

        'xg_class_f1': xg_class_f1,
        'xg_class_report': xg_class_report,
        'xg_acc_score': xg_acc_score,
        'xg_prec_score': xg_prec_score,
        'xg_rec_score': xg_rec_score,
        'xg_f1': xg_f1,
        'xg_confusion_matrix': xg_conf_mat,

        'stack_class_f1': stack_class_f1,
        'stack_class_report': stack_class_report,
        'stack_acc_score': stack_acc_score,
        'stack_prec_score': stack_prec_score,
        'stack_rec_score': stack_rec_score,
        'stack_f1': stack_f1,

        'runtime' : elapsed_time.seconds
    }

    return JsonResponse(data)




