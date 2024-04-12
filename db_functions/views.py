from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the db_functions index!")

def get_entry(request):
    pass

def get_history(request):
    pass

def store_entry(request):
    pass