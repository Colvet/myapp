from django.http import HttpResponse
import json
import pymongo

from MyApplication.MongoDbManager import MongoDbManager
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


from rest_framework.parsers import JSONParser
from MyApplication.serializers import UserSerializer
from django.http.response import JsonResponse

import MyApplication.forms

import logging
logger = logging.getLogger(__name__)

@csrf_exempt
def specific_user(request, username):
    def get():
        dbUserData = MongoDbManager().get_users_from_collection({'name': username})
        responseData = dbUserData[0]
        del responseData['_id']

        return HttpResponse(json.dumps(responseData), status=200)

    def post():
        # try:
        age, job = request.POST['age'], request.POST['job']
        # except:
        #     return HttpResponse(status=400)

        userData = {
            'name': username,
            'age': age,
            'job': job
        }

        result = MongoDbManager().add_user_on_collection(userData)
        return HttpResponse(status=201) if result else HttpResponse(status=500)

    if request.method == 'GET':
        return get()
    elif request.method == 'POST':
        return post()
    else:
        return HttpResponse(status=405)

@csrf_exempt
def add_user(request):
    client = pymongo.MongoClient('localhost',27017)
    db = client.test_database
    collection = db.test_table


    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            collection.insert_one(user_serializer.data)
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        client = pymongo.MongoClient('localhost', 27017)
        db = client.test_database
        collection = db.test_table

        UserData = list(collection.find())

        logger.warning(UserData[0]['age'])


        return HttpResponse(UserData)


@csrf_exempt
def uploadFile(request):
    if request.method == 'POST':
        # form = MyApplication.forms.uploadFileForm(request.POST)
        form = MyApplication.forms.NameForm(request.POST)

        # logger.warning(form)
        # logger.warning("asdfasdfasdf")
        logger.warning(form)
        if form.is_valid():
            form.save()
            return HttpResponse(True)
        else:
            return HttpResponse(False)
        #     logger.warning("file upload success")
        #     return HttpResponse(True)
        # else:
        #     logger.warning("fail")
        #     return HttpResponse(False)





# def fileupload(request):
#     if request.method == 'POST':
#         file =

def all_users(request):
    def get():
        dbUserData = MongoDbManager().get_users_from_collection({})
        responseData = []
        for user in dbUserData:
            del user['_id']
            responseData.append(user)

        return HttpResponse(json.dumps(responseData), status=200)

    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)
