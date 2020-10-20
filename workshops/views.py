from django.http import request
from django.shortcuts import get_object_or_404, render
from .models import Workshop


# Create your views here.
def home_view(request):
    workshops = Workshop.objects.all()
    context = {"workshops": workshops}
    template = 'workshops/home.html'
    return render(request, template, context)


def detail_view(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    context = {'workshop': workshop}
    template = 'workshops/detail.html'
    return render(request, template, context)
