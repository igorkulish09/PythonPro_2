from django.db import models

# Create your models here.

class WeekDay(models.Model):
    title = models.CharField(max_length=20)
    note = models.CharField(max_length=250)

    def __str__(self):
        return f"WeekDay: {self.title}, day note: {self.note}"

class student(models.Model):
    username = models.CharField(max_length=20)
    language = models.CharField(max_length=10)
    grade = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    language = models.CharField(max_length=50, default='English')
    course = models.CharField(max_length=50, blank=True)

    def choose_course(self, course):
        self.course = course
        self.save()

    def get_grade(self):
        return 95

    def __str__(self):
        return self.name

