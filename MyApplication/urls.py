from django.urls import path
from MyApplication.Api import JsonTest

urlpatterns = [
    path('json/', JsonTest.all_users, name='JsonAllUser'),
    path('json/<username>', JsonTest.specific_user, name='JsonSpecificUser'),
    path('add/', JsonTest.add_user),
    path('upload/', JsonTest.uploadFile)
]
