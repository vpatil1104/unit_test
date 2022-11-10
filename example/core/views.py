#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.views.generic.list import ListView

# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'student.html'
    paginate_by = 10
        
        
class StudentView(DetailView):
    model = Student    