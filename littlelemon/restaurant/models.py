from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self) -> str:
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    guests = models.SmallIntegerField()

    def __str__(self):
        return self.name
