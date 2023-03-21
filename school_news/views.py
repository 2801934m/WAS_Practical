from django.shortcuts import render
from django.http import HttpResponse
from school_news.models import NewsItem

def index(request):
    #Query the database for list of all
    NewsItem_list = NewsItem.objects.all

    context_dict = {}
    context_dict['boldmessage'] = 'Top Stories'
    context_dict['NewsItems'] = NewsItem_list

    return render(request, 'school_news/index.html', context=context_dict)


