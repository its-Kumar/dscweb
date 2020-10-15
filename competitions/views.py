from django.http import request
from competitions.models import Competition
from django.shortcuts import get_object_or_404, render


# Create your views here.
def home_view(request):
    competitions = Competition.objects.all().filter(is_active=True)

    template = 'competitions/home.html'
    context = {
        "competitions": competitions,
    }
    return render(request, template_name=template, context=context)


def detail_view(request, pk, slug):
    obj = get_object_or_404(Competition, pk=pk, slug=slug)
    template = 'competitions/detail.html'
    return render(request, template, context={"competition": obj})
