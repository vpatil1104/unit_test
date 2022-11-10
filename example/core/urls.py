from django.urls import path
from . import views
from .test_api_view import CreateStudentApiView

urlpatterns = [
    path('students', views.StudentListView.as_view(), name="students"),
    path('students/create', CreateStudentApiView.as_view(), name="create_student"),
    path('students/<int:id>', views.StudentView.as_view(), name="student_detail"),
]