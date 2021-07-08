from django.shortcuts import render
from positions.models import Position


def positions(request):
    context = {'positions': reversed(Position.objects.all().order_by('end_date'))}
    return render(request, 'positions.html', context)
