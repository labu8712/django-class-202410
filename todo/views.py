from django.shortcuts import render

from todo.models import Project


def project_list(request):
    projects = Project.objects.all()
    return render(
        request,
        "project_list.html",
        {"projects": projects},
    )
