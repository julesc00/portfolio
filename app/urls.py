from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.all_projects, name="all-projects"),
    path('projects/<int:pk>', views.project_detail, name="project-detail"),
]
