import json
import logging
import os
import pymongo
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from myapp.settings import MEDIA_ROOT

from MyApplication.analytics import MakeSummary as ms
import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)

client = pymongo.MongoClient('localhost',27017)
db = client.sixthsense
collection = db.SummaryData


@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        # username = request.POST['username']
        uploadFile = request.FILES['files']
        if uploadFile.name.find('csv') < 0:
            message = "파일형식이 잘못되었습니다"
            print(message)
            # return JsonResponse({"message": message})
        else:
            csv_file = pd.read_csv(uploadFile, encoding='utf8')
            df = pd.DataFrame(csv_file)
            time_now = datetime.now().timestamp()

            if not (os.path.isdir('/Users/Colvet/Documents/Data/'+'test1')):
                print('디렉톨 ㅣ없다 !@#!@#@!#!@#!@#!@#!@#!@')
                os.makedirs(os.path.join('/Users/Colvet/Documents/Data/', 'test1'))

            save_dir = '/Users/Colvet/Documents/Data/' + 'test1/'

            df.to_csv(os.path.join(save_dir, str(time_now)+"_"+uploadFile.name))

            info = ms.analy(df)
            # FileSummaryData = {
            #     "originalLocation": os.path.join(save_dir, str(time_now) + "_" + uploadFile.name),
            #     "fileName": uploadFile.name,
            #     "userName": "request.POST['username']",
            #     "info": info
            # }


            # collection.insert_one(FileSummaryData)
            return HttpResponse(status=400)






# @csrf_exempt
# def specific_user(request, username):
#     def get():
#         dbUserData = MongoDbManager().get_users_from_collection({'name': username})
#         responseData = dbUserData[0]
#         del responseData['_id']
#
#         return HttpResponse(json.dumps(responseData), status=200)
#
#     def post():
#         # try:
#         age, job = request.POST['age'], request.POST['job']
#         # except:
#         #     return HttpResponse(status=400)
#
#         userData = {
#             'name': username,
#             'age': age,
#             'job': job
#         }
#
#         result = MongoDbManager().add_user_on_collection(userData)
#         return HttpResponse(status=201) if result else HttpResponse(status=500)
#
#     if request.method == 'GET':
#         return get()
#     elif request.method == 'POST':
#         return post()
#     else:
#         return HttpResponse(status=405)

# @csrf_exempt
# def add_user(request):
#     client = pymongo.MongoClient('localhost',27017)
#     db = client.test_database
#     collection = db.test_table
#
#
#     if request.method == 'POST':
#         logger.warning("=========")
#         logger.warning(request)
#         logger.warning("==========")
#
#         user_data = JSONParser().parse(request)
#         user_serializer = UserSerializer(data=user_data)
#         if user_serializer.is_valid():
#             collection.insert_one(user_serializer.data)
#             return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
#
#     elif request.method == 'GET':
#         client = pymongo.MongoClient('localhost', 27017)
#         db = client.test_database
#         collection = db.test_table
#
#         UserData = list(collection.find())
#
#         logger.warning(UserData[0]['age'])
#
#
#         return HttpResponse(status=201)

# def all_users(request):
#     def get():
#         dbUserData = MongoDbManager().get_users_from_collection({})
#         responseData = []
#         for user in dbUserData:
#             del user['_id']
#             responseData.append(user)
#
#         return HttpResponse(json.dumps(responseData), status=200)
#
#     if request.method == 'GET':
#         return get()
#     else:
#         return HttpResponse(status=405)
