from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Entity
from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({
        "Success": "true"
    })

def error_view():
    return JsonResponse({
        "status":"not found",
        "Description":"endpoint doesnt exist"
    })