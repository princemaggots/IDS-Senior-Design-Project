from django.http import HttpResponse, JsonResponse
from engine_functions.engine.engine import runLCCDE
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json

@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the engine_functions index!")

@csrf_exempt
def lccde_run(request):
    data = json.loads(request.body)

    dataset = data.get('dataset')
    test_size = float(data.get('test_size', 0.2))
    random_state = int(data.get('random_state', 0))
    sampling_strat2 = int(data.get('sampling_strat2', 1000))
    sampling_strat4 = int(data.get('sampling_strat4', 1000))
    xg_eta = float(data.get('xg_eta', 0.3))
    xg_max_depth = int(data.get('xg_max_depth', 6))
    xg_subsample = float(data.get('xg_subsample', 1))
    xg_lambda = int(data.get('xg_lambda', 1))
    xg_alpha = int(data.get('xg_alpha', 0))
    xg_gamma = int(data.get('xg_gamma', 0))
    xg_colsample_bytree = float(data.get('xg_colsample_bytree', 1))
    xg_min_child_weight = int(data.get('xg_min_child_weight', 1))
    xg_n_estimators = int(data.get('xg_n_estimators', 1))
    cb_iterations = int(data.get('cb_iterations', 1000))
    cb_learning_rate = float(data.get('cb_learning_rate', 0.03))
    cb_depth = int(data.get('cb_depth', 6))
    cb_random_state = int(data.get('cb_random_state', 0))
    cb_loss_function = data.get('cb_loss_function', 'MultiClass')
    lg_boosting = data.get('lg_boosting', 'gbdt')
    lg_learning_rate = float(data.get('lg_learning_rate', 0.1))
    lg_lambda_l1 = float(data.get('lg_lambda_l1', 0))
    lg_num_leaves = int(data.get('lg_num_leaves', 31))
    lg_num_iterations = int(data.get('lg_num_iterations', 100))
    lg_max_depth = int(data.get('lg_max_depth', -1))

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


def mth_run(request):
    pass

def treebased_run(request):
    pass