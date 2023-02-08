from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def User(request):
    return JsonResponse({
        "message": "welcome to megamind"
    })
