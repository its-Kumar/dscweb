import csv

from django.shortcuts import render

from blog.models import BlogPost
from events.models import Event


def home_view(request):
    members = []
    with open("members.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            members.append(i)

    faculty = [
        {
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
        },
    ]
    events = Event.objects.all().filter(is_active=True)
    context = {
        "title": "DSC",
        "members": members,
        "events": events,
        "faculty": faculty,
    }
    return render(request, "home.html", context)


def about_view(request):
    context = {"title": "About Us"}
    return render(request, "about.html", context)


def search_view(request):
    query = request.GET.get("q", None)
    context = {"query": query}
    if query is not None:
        blog_list = BlogPost.objects.search(query=query)
        event_list = Event.objects.search(query=query)
        context["blog_list"] = blog_list
        context["event_list"] = event_list
    return render(request, "search.html", context)
