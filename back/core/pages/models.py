from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)
    quantity_people = models.IntegerField(default=1)
    comments = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




