from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('hello world !')


def index(request):
    print('---------1----------')
    context = {}
    context['hello'] = " Hello the World"
    print(context)
    return render(request, 'hello.html', context)
