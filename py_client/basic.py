# This is our first API client
import requests

endpoint = "https://httpbin.org/status/200/" #Sample endpoints( locations of the resources,)
#endpoint = "https://httpbin.org/"
endpoint = "https://httpbin.org/anything"
get_response = requests.get(endpoint) #HTTP request is made and stored in a variable called get_response
print(get_response.text) # Print source code/raw text code. but by adding '/anyting' ie.REST API we get the data that we can use(JSON or XML)

# HTPP Request -> HTML
# REST API HTPP Request -> JSON/XML
# JSON is very similar to python Dict(only diff is in py 'null' will become 'none') and can be converted to Dict as follows
print(get_response.json())
"""We can send our data as either JSON or raw 'data' and it can be seen reflected in our print statement. 
EX: get_response = requests.get(endpoint, json = {"query" : "Hello World"}) or
    get_response = requests.get(endpoint, data = {"query" : "Hello World"}) In both case the data we sent will be considered differently"""
print(get_response.status_code()) # This shows uss the status code like 200 or 404 etc
