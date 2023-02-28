from django.shortcuts import render, get_object_or_404
from .models import Event
from datetime import datetime

def details(request, id):
    event = get_object_or_404(Event, id=id)
    print(event)
    return render(request, 'events/details.html', {'event': event})


def list(request):
    today = datetime.today()

    filter_map = {
        'title': 'title__icontains',
        'is_free': 'cost'
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value


    events = Event.objects.filter(
          #Greater than or equal to
          datetime__gte=today).filter(**filters).order_by('datetime')
 
    return render(request, 'events/list.html', {'events': events})



