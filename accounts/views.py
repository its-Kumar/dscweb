from accounts.models import Profile
from django.shortcuts import render, redirect
from .forms import CreateUserForm, AccountForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMultiAlternatives


def signupPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            Profile.objects.create(user=user,
                                   first_name=user.first_name,
                                   last_name=user.last_name,
                                   email=user.email)
            html = get_template('registration/Email.html')
            html_content = html.render({'username': username})
            msg = EmailMultiAlternatives(subject="Welcome to DSC",
                                         body=html_content,
                                         to=[email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {"form": form}
    return render(request, 'signup.html', context)


@login_required(login_url='login')
def account_settings(request):
    profile = request.user.profile
    form = AccountForm(instance=profile)
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registration/account_setting.html', context)
