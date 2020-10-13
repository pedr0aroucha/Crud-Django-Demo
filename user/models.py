from django.db import models

class User(models.Model):
  full_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
  age = models.IntegerField(null=False, blank=False)

  def __str__(self):
  	return self.full_name