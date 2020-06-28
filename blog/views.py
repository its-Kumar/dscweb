from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogModelForm, BlogPostForm
# from django.utils import timezone

# Create your views here.


def blog_post_list_view(request):
    # now = timezone.now()
    qs = BlogPost.objects.all().published()
    # qs = BlogPost.objects.filter(publish_date__lte=now)
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (my_qs | qs).distinct()
    template_name = "blog/list.html"
    context = {'object_list': qs}
    return render(request, template_name, context)


@login_required
def blog_post_create_view(request):
    form = BlogModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data
        data['user'] = request.user
        obj = BlogPost.objects.create(**data)
        form = BlogPostForm()
    template_name = "form.html"
    context = {'form': form}
    return render(request, template_name, context)


"""
@login_required
def blog_post_create_view(request):
    form = BlogModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save(commit=False)
        form.user = request.user
        form.save()
        form = BlogModelForm()
    template_name = "form.html"
    context = {'form': form}
    return render(request, template_name, context)
"""
@login_required
def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


@login_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    template_name = "form.html"
    context = {'form': form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)


@login_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context = {"object": obj}
    return render(request, template_name, context)
