from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from events.models import Event


# Create your views here.
def home_view(request):
    queryset = Event.objects.all()
    paginator = Paginator(queryset, 25)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    template = "events/home.html"
    context = {
        "events": events,
    }
    return render(request, template_name=template, context=context)


def detail_view(request, pk, slug):
    obj = get_object_or_404(Event, pk=pk, slug=slug)
    template = "events/detail.html"
    return render(request, template, context={"event": obj})
