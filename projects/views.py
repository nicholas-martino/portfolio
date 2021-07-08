from django.shortcuts import render
from projects.models import Project
from positions.models import Position


def project_index(request):
    context = {
        'projects': reversed(Project.objects.all().order_by('date')),
        'positions': list(reversed(Position.objects.all().order_by('end_date')))
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    context = {'project': Project.objects.get(pk=pk)}
    return render(request, 'project_detail.html', context)
