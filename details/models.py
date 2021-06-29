from django.core.checks.messages import CheckMessage
from django.db import models

# Create your models here.
class Contact(models.Model):
    formFilled: bool
    createdBy = models.CharField(max_length=122, default="NULL")
    selects = models.BooleanField(default=False)
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122) 
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    # fullName = models.CharField(max_length=122)
    # fullName = fname + " " + lname
    address = models.TextField()
    date = models.DateField()

    def __str__(self):
            return self.fname + " " + self.lname 