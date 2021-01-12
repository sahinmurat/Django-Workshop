from django.shortcuts import render
from django.http import JsonResponse
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status


def home_api(request):
    data = {
        "name": "henry",
        "address": "clarusway.com",
        "skills": ["python", "django"]
    }
    return JsonResponse(data)


# def student_list_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         student_count = Student.objects.count()

#         student_list = []
#         for student in students: # mevlüt, henry
#             student_list.append({
#                 "fisrtname": student.first_name,
#                 "lastname": student.last_name,
#                 "number": student.number
#             })
#         print(student_list)

#         data = {
#             "students": student_list,
#             "count": student_count
#         }
#         return JsonResponse(data)

def student_list_api(request):
        if request.method == 'GET':
            students = Student.objects.all()
            student_count = Student.objects.count()
            student_list = serialize('python', students)
            data = {
                'student': student_list,
                'count': student_count
            }
            print(data)
            return JsonResponse(data)