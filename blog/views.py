from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# """
# request = обьект класса HttpRequest, который формирует из запроса от клиента на наш сервер 
# """


def get_hello(request):
    return HttpResponse("Hello", headers={"Name": "Alex"}, status=500)

def get_contact(request):
    return HttpResponse("number")

def get_about(request):
    return HttpResponse("about")