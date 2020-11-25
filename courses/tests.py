from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Course, Step


class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in Python.",
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing", description="Learn to write tests in python"
        )
        self.course2 = Course.objects.create(
            title="New Course", description="A new course"
        )
        self.step = Step.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in your docstrings.",
            course=self.course,
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse("list"))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context["courses"])
        self.assertIn(self.course2, resp.context["courses"])
