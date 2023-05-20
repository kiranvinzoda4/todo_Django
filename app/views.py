from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import user, todo
from .serializers import UserSerializer, TodoSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from . import curd
from . import auth
import base64


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        user_data = curd.login(request)
        if user_data == False :
            return JsonResponse({"error" : "email or password is wrong"}, safe=False)
        serializer = UserSerializer(user_data, many = False)
        return JsonResponse({"user" : serializer.data, "token" : auth.encode_token(user_data.id)}, safe=False)
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)    


@csrf_exempt
def get_all_users(request):
    if request.method == "GET":
        user_data = curd.get_all_users()
        serializer = UserSerializer(user_data, many = True)
        return JsonResponse({"user" : serializer.data}, safe=False)
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)   

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        user_data = curd.add_user(request)
        serializer = UserSerializer(user_data, many = False)
        return JsonResponse({"user" : serializer.data}, safe=False) 
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)     

@csrf_exempt
def get_user(request, id):
    if request.method == "GET":
        user_data = curd.get_user_by_id(id)
        serializer = UserSerializer(user_data, many = False)
        return JsonResponse({"user" : serializer.data}, safe=False) 
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)    
    
@csrf_exempt
def update_user(request, id):
    if request.method == "POST":
        user_data = curd.update_user_by_id(id, request)
        serializer = UserSerializer(user_data, many = False)
        return JsonResponse({"user" : serializer.data}, safe=False)
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)     

@csrf_exempt
def delete_user(request, id):
    if request.method == "GET":
        user_data = curd.delete_user_by_id(id)
        serializer = UserSerializer(user_data, many = False)
        return JsonResponse({"user" : serializer.data}, safe=False)
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)     


# views function of todo


@csrf_exempt
def get_all_todos(request):
    if request.method == "GET":
        check = curd.user_varification(request.headers.get('token'))
        if check :  
            todo_data = curd.get_all_todos()
            serializer = TodoSerializer(todo_data, many = True)
            return JsonResponse({"todo" : serializer.data}, safe=False)
        else:
            return JsonResponse({"error" : "unathorized user"}, safe=False) 
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)    

@csrf_exempt
def create_todo(request):
    if request.method == "POST":
        check = curd.user_varification(request.headers.get('token'))
        if check :
            todo_data = curd.add_todo(request)
            serializer = TodoSerializer(todo_data, many = False)
            return JsonResponse({"todo" : serializer.data}, safe=False) 
        else:
            return JsonResponse({"error" : "unathorized user"}, safe=False)    
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)     

@csrf_exempt
def get_todo(request, id):
    if request.method == "GET":
        check = curd.user_varification(request.headers.get('token'))
        if check :
            todo_data = curd.get_todo_by_id(id)
            if todo_data is None:
                return JsonResponse({"error" : "Todo not found"}, safe=False)
            if todo_data.img != None:
                with open(todo_data.img, "rb") as image2string:
                    converted_string =  'data:image/jpg;base64,'+base64.b64encode(image2string.read()).decode()
                todo_data.img = converted_string
            else:
                todo_data.img = None
            serializer = TodoSerializer(todo_data, many = False)
            return JsonResponse({"todo" : serializer.data}, safe=False)
        else:
            return JsonResponse({"error" : "unathorized user"}, safe=False)    
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)     
    
@csrf_exempt
def update_todo(request, id):
    if request.method == "POST":
        check = curd.user_varification(request.headers.get('token'))
        if check :
            todo_data = curd.update_todo_by_id(id, request)
            serializer = TodoSerializer(todo_data, many = False)
            return JsonResponse({"todo" : serializer.data}, safe=False)
        else:
            return JsonResponse({"error" : "unathorized user"}, safe=False)    
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)     

@csrf_exempt
def delete_todo(request, id):
    if request.method == "GET":
        check = curd.user_varification(request.headers.get('token'))
        if check :
            todo_data = curd.delete_todo_by_id(id)
            serializer = TodoSerializer(todo_data, many = False)
            return JsonResponse({"todo" : serializer.data}, safe=False)
        else:
            return JsonResponse({"error" : "unathorized user"}, safe=False)    
    else:
        return JsonResponse({"error" : "request method is not valid"}, safe=False)     

