from django.shortcuts import get_object_or_404, render

from .models import Course, Step


def course_list(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "courses/course_list.html", context)


def course_detail(request, pk):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk)
    context = {"course": course}
    return render(request, "courses/course_detail.html", context)


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    context = {"step": step}
    return render(request, "courses/step_detail.html", context)
