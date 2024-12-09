from deepakGPAconversion import gpa_to_percentage
from django.db import models


# Create your models here.
class Student(models.Model):
  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()
  percentage = models.FloatField(editable=False, null=True, blank=True)

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'
  
  def save(self, *args, **kwargs):
        self.percentage = gpa_to_percentage(self.gpa)
        super().save(*args, **kwargs)
