#from statistics import mode
from django.forms import model_to_dict
#from django.shortcuts import render
#from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product


@api_view(["GET"]) #This decorator and returning the Response make this a Django Rest Framework
def api_home(request, *args, **kwargs):
    
    #The request we are taking in as parameter above is the HTTP instance request from django
    """ print(request.GET) # We have added this to echo our query parameters params={"abc": 123}. request.GET will get the reqquest parameters
    print(request.POST)
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
    #We dont want to hardcode data as above so we will create a variable data which can take values and then return it.
        data['parmas'] = dict(request.GET) # This brings back the parameter and display "abc=123"
    data['headers'] = dict(request.headers) # We get the header
    data['content_type'] = request.content_type
    
    """
    # now we will grab the data from the app we have built "products"
    model_data = Product.objects.all().order_by("?").first() #This makes random queryset and grabs one of the value
    data = {}
    """
    if model_data:
        # data['id'] = model_data.id
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price
        #data = model_to_dict(model_data) #This is equivalent to the above four lines
        data = model_to_dict(model_data, fields= ['id', 'title']) #We can decide what fields we want to display

        # now we want our model instance(model_data) to be turned into a python Dict and then return JSON to the client
    return JsonResponse(data)
    """
    if model_data:
        data = model_to_dict(model_data, fields= ['id', 'title'])
    return Response(data)