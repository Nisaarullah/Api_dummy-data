from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='card_images/')
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
