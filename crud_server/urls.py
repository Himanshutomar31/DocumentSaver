from django.urls import path, include
from crud_server.views import test 

urlpatterns = [
   path('test/',test)
]
