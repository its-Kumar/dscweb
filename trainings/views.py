from django.http import request
from django.shortcuts import get_object_or_404, render
from .models import Training


# Create your views here.
def home_view(request):
    trainings = Training.objects.all()
    context = {"trainings": trainings}
    template = 'trainings/home.html'
    return render(request, template, context)


def detail_view(request, pk):
    training = get_object_or_404(Training, pk=pk)
    context = {'training': training}
    template = 'trainings/detail.html'
    return render(request, template, context)
 