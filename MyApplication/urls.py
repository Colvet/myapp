from django.urls import path
from MyApplication.Api import JsonTest
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('json/', JsonTest.all_users, name='JsonAllUser'),
    # path('json/<username>', JsonTest.specific_user, name='JsonSpecificUser'),
    # path('add/', JsonTest.add_user),
    path('upload/', JsonTest.my_view, name='my-view')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
