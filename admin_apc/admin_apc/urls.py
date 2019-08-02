"""admin_apc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from interface import views
from django.urls import path
from admin_apc import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='url_index'),
    path('choose_students/', views.choose_students, name='choose_students'),
    path('students/', views.students, name='url_students'),
    path('create_student/', views.create_student, name='create_student'),
    path('update_student/', views.update_student, name='update_student'),
    path('choose_classes/', views.choose_classes, name='choose_classes'),
    path('classes/', views.classes, name='url_classes'),
    path('create_class/', views.create_class, name='create_class'),
    path('update_class/', views.update_class, name='update_class'),
    path('choose_news/', views.choose_news, name='choose_news'),
    path('news/', views.news, name='url_news'),
    path('create_new/', views.create_new, name='create_new'),
    path('update_new/', views.update_new, name='update_new'),
    path('choose_exams/', views.choose_exams, name='choose_exams'),
    path('exams/', views.exams, name='url_exams'),
    path('create_exam/', views.create_exam, name='create_exam'),
    path('update_exam/', views.update_exam, name='update_exam'),
    path('create_task/', views.create_task, name='create_task'),
    path('update_task/', views.update_task, name='update_task'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
