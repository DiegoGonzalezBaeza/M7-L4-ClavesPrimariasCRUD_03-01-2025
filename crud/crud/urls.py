"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from app2 import views as views2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list, name='student_list'),
    path('student/create/', views.student_create, name='student_create'),
    #http://edutecno.com/estudiante/1/
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    #http://edutecno.com/estudiante/2/update/
    path('student/<int:pk>/update/', views.student_update, name='student_update'),
    #http://edutecno.com/estudiante/3/delete/
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),

    path('course/list', views2.course_list, name='course_list'),
    path('course/create/', views2.course_create, name='course_create'),
    #http://edutecno.com/course/1/
    path('course/<int:pk>/', views2.course_detail, name='course_detail'),
    #http://edutecno.com/course/2/update/
    path('course/<int:pk>/update/', views2.course_update, name='course_update'),
    #http://edutecno.com/course/3/delete/
    path('course/<int:pk>/delete/', views2.course_delete, name='course_delete'),
]
