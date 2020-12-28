from django.contrib import admin
from django.urls import path
from . import views
app_name = "sandforce"
urlpatterns = [
    path('', views.index,name="index"),
    path('project-detail/<project_id>/', views.project_details,name="project-detail"),
    path('contact_record/', views.contact_record,name="contact_record"),
]
