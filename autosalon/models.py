from django.db import models


class CarModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'CarModel'
        verbose_name_plural = 'CarModels'


class User(models.Model):
    name = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    phone_number = models.IntegerField(default='XX XXX-XX-XX')
    passport = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Order(models.Model):
    TYPE_CHOICES = (
        ('Automatic', 'Automatic'),
        ('Mechanic', 'Mechanic'),
        ('Electronic', 'Electronic')
    )
    POSITION_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    PRODUCTION_CHOICES = (
        ('Local', 'Local'),
        ('Export', 'Export'),
        ('Import', 'Import')
    )
    COLOR_CHOICES = (
        ('Green', 'Green'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Pink', 'Pink'),
    )
    STATUS_CHOICES = (
        ('In Order', 'In Order'),
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
        ('In Way', 'In Way'),
        ('Order Completed', 'Order Completed')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, null=True, blank=True)
    production = models.CharField(max_length=100, choices=PRODUCTION_CHOICES)
    year = models.IntegerField(default=2021)
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)
    Additional = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.user.name} ordered product: {self.name}"
