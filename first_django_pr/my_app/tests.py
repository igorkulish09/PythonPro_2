from django.test import TestCase
from django.urls import reverse
import pytest
from pytest_django.asserts import assertQuerysetEqual
from .models import WeekDay, Note


# Create your tests here.
@pytest.mark.urls("my_app.urls")
def test_index_redirects_to_my_week(client):
    response = client.get("/")
    assert response.status_code == 302
    assert response.url == reverse("my_week")


@pytest.mark.django_db
def test_my_week_has_three_days(client):
    response_clean_database = client.get("/week/")
    weeks_days = WeekDay.objects.all()
    assertQuerysetEqual(response_clean_database.context["days"], weeks_days)
    for day in ["Mon", "Tue", "Wed"]:
        WeekDay.objects.create(day=day)
    weeks_days_updated = WeekDay.objects.all()
    response_fulfilled_database = client.get("/week/")
    assertQuerysetEqual(
        response_fulfilled_database.context["days"], weeks_days_updated, ordered=False
    )
    assert len(response_fulfilled_database.context["days"]) == 3


# Homework7. Tests in Django


class RoutingTestCase(TestCase):
    def test_week_day_route(self):
        response = self.client.get(reverse("my_week"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b"Week Plans")


class DatabaseTestCase(TestCase):
    def setUp(self):
        self.day1 = WeekDay.objects.create(day="Day1")
        self.day2 = WeekDay.objects.create(day="Day2")
        self.note1 = Note.objects.create(
            week_day=self.day1, title="Note1", msg="Message1"
        )
        self.note2 = Note.objects.create(
            week_day=self.day2, title="Note2", msg="Message2"
        )
        self.note3 = Note.objects.create(
            week_day=self.day2, title="Note3", msg="Message3"
        )
        self.note4 = Note.objects.create(
            week_day=self.day2, title="Note4", msg="Message4"
        )

    def test_day_detail_context(self):
        response = self.client.get(reverse("week_day", args=[self.day1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["object"].notes.all()), 1)

        response = self.client.get(reverse("week_day", args=[self.day2.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["object"].notes.all()), 3)
