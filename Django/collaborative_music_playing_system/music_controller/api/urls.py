# store the urls local to this api app 

from django.urls import path
from .views import main 

urlpatterns = [
    path('', main),

]
