from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from db_functions.models import Result
from datetime import datetime
from django.core.serializers import serialize


@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the db_functions index!")

@csrf_exempt
def get_entry(request):
    # request_body = json.loads(request.body.decode('utf-8'))
    # queryset = Result.objects.filter(id = request_body['entry_id'])
    id = request.GET.get('entry_id')
    queryset = Result.objects.filter(id = id)
    return JsonResponse(queryset[0].format_output_json())

@csrf_exempt
def get_history(request):
    all_entries = Result.objects.all().order_by("id").all()
    print(all_entries)
    data = serialize('json', all_entries)
    return JsonResponse(data=data, safe=False)

@csrf_exempt
def delete_entry(request):
    id = request.GET.get('entry_id')
    instance = Result.objects.filter(id = id)
    instance.delete()
    return HttpResponse({"message": "Data Successfully Deleted!"})

@csrf_exempt
def store_entry(request):
    print("Saving...")
    request_body = json.loads(request.body.decode('utf-8'))
    now = datetime.now()
    instance = Result(request_timestamp=now, runtime=request_body['output']['runtime'], dataset=request_body['input']['dataset'], model=request_body['input']['model'], input_json=str(request_body['input']), stack_precision=request_body['output']['stack_prec_score'], stack_accuracy=request_body['output']['stack_acc_score'], stack_f1=request_body['output']['stack_f1'], stack_recall=request_body['output']['stack_rec_score'], output_json=str(request_body['output']))
    instance.save()
    return JsonResponse({"message": "Data Successfully Saved!"})