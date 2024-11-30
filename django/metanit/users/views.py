from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from users.forms import AddPostForm


def index(request):
    return render(request, 'htmlfile/index.html')

def about(request):
    return render(request, 'htmlfile/about.html')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def addpage(request):
    form = AddPostForm()
    data = {
        'form' : form
    }
    return render(request, 'htmlfile/index.html', data)