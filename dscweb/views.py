from events.models import Event
from django.shortcuts import render, get_object_or_404
import csv


def home_view(request):
    members = []
    with open('members.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            members.append(i)

    faculty = [{
        "name": "Santosh Kumar",
        "email": "santosh.recb@gmail.com",
        "area": "Networking, Algorithms, SDN",
        "image": "http://recb.ac.in/FacultyPhoto/Faculty21313_20072019012028.jpg",
    },
        {
        "name": "Sudhir Goswami",
        "email": "sudhirgoswami.recb@gmail.com",
        "area": "Image Processing and Algorithm Design",
        "image": "http://recb.ac.in/FacultyPhoto/Faculty04512_20072019012212.JPG",
    }]
    events = Event.objects.all().filter(is_active=True)
    context = {
        "title": "DSC",
        "members": members,
        "events": events,
        "faculty": faculty,
    }
    return render(request, 'home.html', context)


def about_view(request):
    context = {"title": 'About Us'}
    return render(request, 'about.html', context)
