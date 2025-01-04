from django.db import models
from app2.models import Course

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.course}'