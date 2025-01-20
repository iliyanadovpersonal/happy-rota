from django.db import models

class Rota(models.Model):
    day = models.CharField(max_length=3)  # e.g., MON, TUE
    date = models.DateField()

    def __str__(self):
        return f"{self.day} {self.date}"

class RotaRow(models.Model):
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE, related_name="rows")
    employee_name = models.CharField(max_length=100)
    preferences = models.JSONField(default=dict)  # {"MON": "1", "TUE": "X"}

    def __str__(self):
        return self.employee_name
