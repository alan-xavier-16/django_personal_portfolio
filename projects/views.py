from django.shortcuts import render
from projects.models import Project


def project_index(request):
    """View function for index page showing snippets of each project

    Args:
        request: HttpRequest
    """
    # Query collects all abjects from Projects table in database
    projects = Project.objects.all()
    # Context dictionary to send to template
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    """View function for index page showing snippets of each project

    Args:
        request: HttpRequest
        pk: Primary Key
    """
    # Query retrieves the project with primary key, pk
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
