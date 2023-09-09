from django.db import models

# Create your models here.
class Record(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.first_name} - {self.last_name}")  
