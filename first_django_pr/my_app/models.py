from django.db import models

# Create your models here.
class WeekDay(models.Model):
    day = models.CharField(max_length=20)

    def __str__(self):
        return f"Week Day: {self.day}"

class Note(models.Model):
    week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    msg = models.CharField(max_length=250)

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

