from django.shortcuts import render
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    #The request we are taking in as parameter above is the HTTP instance request from django
    body = request.body #byte string of JSON data
    print(body)
    return JsonResponse({"message": "Hi there, this is your Django API response!!"})
