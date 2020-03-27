from django.shortcuts import render
from .forms import MemberForm
from .models import Member

def home_view(request):
    context = {"title": "DSC"}
    return render(request, 'home.html', context)

def about_view(request):
    context = {"title": 'About Us'}
    return render(request, 'about.html', context)

def register_view(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        obj = Member(username=data['username'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    mobile=data['mobile'],
                    email=data['email'],
                    password=data['password'])
        obj.save()
        form = MemberForm()
    context = {"form": form, "title":"Register"}
    return render(request, 'form.html', context)

