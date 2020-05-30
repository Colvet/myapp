from django.http import HttpResponse
import json
import pymongo

from MyApplication.MongoDbManager import MongoDbManager
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

import csv
from rest_framework.parsers import JSONParser
from MyApplication.serializers import UserSerializer
from django.http.response import JsonResponse

from MyApplication.forms import DocumentForm
from MyApplication.models import Document

from django.shortcuts import redirect, render

import pandas as pd
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
        logger.warning("=========")
        logger.warning(request)
        logger.warning("==========")

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


# @csrf_exempt
# def uploadFile(APIView):
#         parser_classes = (MultiPartParser, FormParser)
#
#         # file_serializer = FileSerializer(data=request.data)
#
#         # file_data = csv_file.read().decode("utf-8")
#
#         parser_classes = (MultiPartParser, FormParser)
#
#         def post(self, request, *args, **kwargs):
#             file_serializer = FileSerializer(data=request.data)
#             if file_serializer.is_valid():
#                 file_serializer.save()
#                 return HttpResponse(file_serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return HttpResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def fileupload(request):
#     if request.method == 'POST':
#         file =


@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])

            uploadFile=request.FILES['docfile']
            if uploadFile.name.find('csv') < 0:
                message = "파일형식이 잘못되었습니다"

                return JsonResponse({"message": message})

            csv_file = pd.read_csv(uploadFile, encoding='utf8')
            df = pd.DataFrame(csv_file)
            # csv_file.to_json()
            print(df)
            print(df.dtypes)
            print(df.describe())
            print(df.to_numeric())

            # newdoc.save()



            return redirect('my-view')
            # return HttpResponse(True)
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form}
    return render(request, 'list.html', context)











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
