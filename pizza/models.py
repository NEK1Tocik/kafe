from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PizzaItem(models.Model):
    name = models.TextField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    price = models.FloatField(verbose_name='цена', default=0.00)
    image_url = models.TextField()

    def __str__(self):
        return f'{self.name}'


class BasketItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(PizzaItem, on_delete=models.CASCADE)
    readiness = models.BooleanField(verbose_name='готвность', default=False)


class UserTG(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TG_id = models.TextField(verbose_name='телеграм ID', default=None)


class Order(models.Model):
    order_id = models.IntegerField(
        verbose_name='номер заказа',
        unique=True,
        auto_created=True
    )
    unprocessed = models.BooleanField(
        verbose_name='необработан',
        default=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(PizzaItem, on_delete=models.CASCADE)
    pass


class Flags(models.Model):
    name = models.TextField()
    description = models.TextField()
    condition = models.BooleanField()

    def __str__(self):
        return self.condition