from django.db import models
from django.contrib.auth.models import User

class Day(models.Model):
    name = models.CharField(max_length=3)  # E.g., MON, TUE
    date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.date}"

class Preference(models.Model):
    PREFERENCE_CHOICES = [
        ('X', 'Unavailable'),
        ('1', 'Preferred'),
        ('2', 'Second Choice'),
        ('L', 'Leave'),
        ('', 'Empty'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    preference = models.CharField(max_length=1, choices=PREFERENCE_CHOICES, blank=True)

    def __str__(self):
        return f"{self.employee.username} - {self.day.name} - {self.preference}"
