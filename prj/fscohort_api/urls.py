from django.urls import path
from .views import home_api, student_list_api

urlpatterns = [
    path("home-api/", home_api, name="home_api"),
    path("list-api/",student_list_api),
 
    # path("about/", about)
]
# localhost/1/delete