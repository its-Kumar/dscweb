from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import redirect, render
from django.template.loader import get_template

from accounts.models import Profile

from .forms import AccountForm, CreateUserForm


def signupPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            html = get_template("registration/Email.html")
            html_content = html.render({"username": username})
            msg = EmailMultiAlternatives(
                subject="Welcome to DSC", body=html_content, to=[email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, "Account was created for " + username)
            return redirect("login")

    context = {"form": form}
    return render(request, "signup.html", context)


@login_required(login_url="login")
def account_settings(request):
    if Profile.objects.all().filter(user=request.user).exists():
        profile = request.user.profile
    else:
        profile = Profile.objects.create(
            user=request.user,
            first_name=request.user.first_name,
            last_name=request.user.last_name,
            email=request.user.email,
        )
    print(profile)
    form = AccountForm(instance=profile)
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "registration/account_setting.html", context)
