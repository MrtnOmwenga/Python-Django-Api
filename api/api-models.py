from unittest.util import _MAX_LENGTH
from django.db import models

# Employee table.
class Employees(models.Model):
    name = models.CharField(max_length = 255)
    id = models.CharField(max_length = 12, primary_key=True)
    department = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)