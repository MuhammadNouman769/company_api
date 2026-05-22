
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/create/', views.create_student, name='create_student'),
]
