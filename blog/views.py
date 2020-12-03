from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogModelForm, CommentForm
from .models import BlogPost

# from django.utils import timezone

# Create your views here.


def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (my_qs | qs).distinct()
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template_name = "blog/list.html"
    context = {"object_list": posts}
    return render(request, template_name, context)


@login_required
def blog_post_create_view(request):
    form = BlogModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data
        data["user"] = request.user
        obj = BlogPost.objects.create(**data)
        return redirect("/blog")

    template_name = "form.html"
    context = {"form": form}
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


def blog_post_detail_view(request, slug):

    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    template_name = "blog/detail.html"
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        "blog_post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }
    return render(request, template_name, context)


@login_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogModelForm(request.POST or None,
                         request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(f"{obj.get_absolute_url()}")
    template_name = "form.html"
    context = {"form": form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)


@login_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)
