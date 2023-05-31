from django.db import models

# Create your models here.
class WeekDay(models.Model):
    day = models.CharField(max_length=20)

    def __str__(self):
        return f"Week Day: {self.day}"

class Note(models.Model):
    week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=100)
    msg = models.CharField(max_length=250)
    assignee = models.CharField(max_length=100, blank=True, null=True) #додав
    email = models.EmailField(blank=True, null=True) # додав


