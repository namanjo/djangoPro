from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'my_tag': "Hello i am from views.py"}
    return render(request, 'app_one/index.html', context=my_dict)
