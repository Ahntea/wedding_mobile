from django.db import models

# Create your models here.
class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table='firstapp_curriculum'

        app_label = 'firstapp'

        ordering = ['-id', 'name']

class Customer(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=10)
    c_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)