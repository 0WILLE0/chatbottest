from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
import requests

def keyboard (request) :
    return JsonResponse(
        {
            "type" : "buttons",
            "buttons" : ["인사", "", "선택 3"],
        }
    )

@csrf_exempt
def message(request) :
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']  #버튼 항목중 무엇을 눌렀는가
    
    if return_str == '인사' :
        return JsonResponse({
           "message" : {
               "text" : "안녕하세요" 
               }
        })
    if return_str == '인사' :
        return JsonResponse({
           "message" : {
               "text" : "안녕하세요" 
               }
        })
    if return_str == '인사' :
        return JsonResponse({
           "message" : {
               "text" : "안녕하세요" 
               }
        })