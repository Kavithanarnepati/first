from django.shortcuts import render

# Create your views here.


from django.http import HttpRsponse


def string_Response(request):
    return HttpRsponse('This is my first string ')