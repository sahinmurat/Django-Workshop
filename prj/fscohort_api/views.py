from django.shortcuts import render, redirect
from django.http import JsonResponse
from fscohort.models import Student

# Create your views here.
def home_api(request):
    data = {
        'name': 'Henry',
        'adress': 'clarusway.igersheim',
        'skills': ['python', 'django']
    }
    
    return JsonResponse(data)

def student_list_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_count = Student.objects.count()
        
        student_list = []
        for student in students:
            student_list.append({
                'first_name':student.first_name,
                'last_name': student.first_name,
                'number': student.number,
            })
            
        data = {
           'students': student_list,
            'count': student_count
        }
        
        return JsonResponse(data)