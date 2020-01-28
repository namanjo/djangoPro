from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import Topic, Webpage, AccessRecord, UserInfo

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    user_list = UserInfo.objects.order_by('first_name')
    data_dict = {'webpage_list':webpages_list, 'user_list': user_list}
    return render(request, 'app_one/index.html', context=data_dict)
