from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hospitals/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    email = models.EmailField(max_length=254)
    openhours = models.IntegerField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    age = models.IntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    title = models.CharField(max_length=100)
    experience = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    email = models.EmailField(max_length=254)
    hours = models.IntegerField()
    linkedin_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name