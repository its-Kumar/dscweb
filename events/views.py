from events.models import Event
from django.shortcuts import get_object_or_404, render


# Create your views here.
def home_view(request):
    events = Event.objects.all()

    template = 'events/home.html'
    context = {
        "events": events,
    }
    return render(request, template_name=template, context=context)


def detail_view(request, pk, slug):
    obj = get_object_or_404(Event, pk=pk, slug=slug)
    template = 'events/detail.html'
    return render(request, template, context={"event": obj})
