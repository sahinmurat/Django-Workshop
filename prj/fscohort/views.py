from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

def about_view(request):
    return HttpResponse('about')

def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    # return HttpResponse("Hi, this is fscohort Home page.")
    form = StudentForm()
    
    my_context = {
        "title": "clarusway",
        "dict_1": {"django": "best framwort"},
        "my_list": [1, 2, 3, 4],
        'student' : form
    }
    return render(request, "fscohort/home.html", my_context)



