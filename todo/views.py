from django.shortcuts import redirect, render

from todo.forms import ProjectForm
from todo.models import Project


def project_list(request):
    projects = Project.objects.all()
    return render(
        request,
        "project_list.html",
        {"projects": projects},
    )


def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("project-list")

    return render(request, "project_create.html", {"form": form})
