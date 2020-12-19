from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from app.models import Project


def index(request):
    context = {
        "title": "My Portfolio"
    }
    return render(request, "app/index.html", context)


def all_projects(request):
    """Show all projects"""
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "app/all_projects.html", context)


def project_detail(request, pk):
    """Query one project."""
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "app/project_detail.html", context)
