from django.urls import path 
from .views import StudentList, StudentGetUpdateDelete,  home_api, student_list_api , student_list_create_api,student_get_update_delete

urlpatterns = [
    path('home-api', home_api),
    path('list-api', student_list_api),
      path("<int:id>/", StudentGetUpdateDelete.as_view(), name="detail"),
    # path('list-create-api', student_list_create_api),
    path('list-create-api', StudentList.as_view()),
    path('<int:id>/', student_get_update_delete),
    # path('list-create-api', student_create_api),
    # path('create-api', create_student),
]
