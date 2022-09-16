from django.db import models

# Create your models here.
class Task(models.Model):
    t_name=models.CharField(max_length=300)
    t_priority=models.IntegerField()
    t_date=models.DateField()

    def __str__(self):
        return  self.t_name