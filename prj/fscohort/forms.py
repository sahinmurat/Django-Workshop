from django.db.models import fields
# from prj.fscohort.models import Student
from django import forms
from django.db import models
from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=20)
#     last_name = forms.CharField(max_length=20)
#     number = forms.IntegerField()

class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label='huhu')
    class Meta:
        model = Student
        fields =  '__all__' 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['last_name'].label = 'My Surname'
        