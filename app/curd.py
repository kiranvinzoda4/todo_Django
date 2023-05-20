from .models import user, todo
import uuid
import json
from . import auth
import base64

def generate_id():
    id = str(uuid.uuid4())
    return id


def login(request):
    request_data = json.loads(request.body)
    email = request_data['email']
    password = request_data['password']
    user_data = user.objects.get(email = email, is_deleted = False)
    hash_password = user_data.password
    check = auth.verify_password(password, hash_password)
    if check:
        return user_data
    else:
        return False


def user_varification(token):
    result_id = auth.decode_token(token)
    user_record = user.objects.get(id = result_id)
    if user_record is not None:
        return True
    else:
        return False

def get_user_by_token(token):
    result_id = auth.decode_token(token)
    user_record = user.objects.get(id = result_id)
    return user_record

def get_all_users():
    data = user.objects.filter(is_deleted = False).all()
    return data

def add_user(request):
    request_data = json.loads(request.body)
    name = request_data['name']
    email = request_data['email']
    password = auth.get_password_hash(request_data['password'])
    id = generate_id()
    data = user()
    data.id = id
    data.name = name
    data.email = email
    data.password = password
    data.save()
    data = user.objects.get(id = id)
    return data

def get_user_by_id(id):
    data = user.objects.get(id = id, is_deleted = False)
    return data


def update_user_by_id(id, request):
    request_data = json.loads(request.body)
    name = request_data['name']
    email = request_data['email']
    password = request_data['password']
    data = user.objects.get(id = id)
    data.name = name
    data.email = email
    data.password = password
    data.save()
    data = user.objects.get(id = id)
    return data

def delete_user_by_id(id):
    data = user.objects.get(id = id)
    data.is_deleted = True
    data.save()
    data = user.objects.get(id = id)
    return data


# todo


def get_all_todos():
    data = todo.objects.filter(is_deleted = False).all()
    return data

def add_todo(request):
    request_data = json.loads(request.body)
    title = request_data['title']
    desc = request_data['desc']
    user_id = request_data['user']
    img = request_data['img']
    if img != "":
        head, data = img.split(',', 1)
        file_ext = head.split(';')[0].split('/')[1]
        plain_data = base64.b64decode(data)
        file_name = generate_id()
        file_location = f"files/{file_name}."
        with open(file_location + file_ext, 'wb') as f:
            f.write(plain_data)
        img_path = "files/"+file_name+"."+file_ext 
    else:
        img_path = None 
    user_obj = user.objects.get(id = user_id)
    id = generate_id()
    data = todo()
    data.id = id
    data.title = title
    data.desc = desc
    data.user = user_obj
    data.img = img_path
    data.save()
    data =  todo.objects.get(id = id)
    return data

def get_todo_by_id(id):
    data = todo.objects.get(id = id, is_deleted = False)
    return data

def update_todo_by_id(id, request):
    request_data = json.loads(request.body)
    title = request_data['title']
    desc = request_data['desc']
    img = request_data['img']
    todo_data = todo.objects.get(id = id)
    if img != "":
        head, data = img.split(',', 1)
        file_ext = head.split(';')[0].split('/')[1]
        plain_data = base64.b64decode(data)
        if todo_data.img == "":
            file_location = "files/"+todo_data.id+"."+file_ext 
            with open(file_location, 'wb') as f:
                f.write(plain_data)  
        else:
            file_location = todo_data.img 
        with open(file_location, 'wb') as f:
            f.write(plain_data)  
    else:
        file_location = None 
    todo_data.title = title
    todo_data.desc = desc
    todo_data.img = file_location
    todo_data.save()
    data = todo.objects.get(id = id)
    return data

def delete_todo_by_id(id):
    data = todo.objects.get(id = id)
    data.is_deleted = True
    data.save()
    data = todo.objects.get(id = id)
    return data
