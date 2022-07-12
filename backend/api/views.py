from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    #The request we are taking in as parameter above is the HTTP instance request from django
    body = request.body #byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data ie. Pyhton dict
    except:
        pass
    # We have added the exception handling because there might be a case where our application might not have json data
    # print(body)
    print(data)# we can also pring data.keys
    #return JsonResponse({"message": "Hi there, this is your Django API response!!"})
    """We don't want to hardcode data as above so we will create a variable data which can take values and then return it.
    """
    data['headers'] = dict(request.headers) # We get the header
    data['content_type'] = request.content_type
    return JsonResponse(data)