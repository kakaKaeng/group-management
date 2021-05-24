from django.db import models
from model_controller.models import AbstractSoftDeletionModelController, AbstractModelController

from management.apps.commons.constants import CHAR_NULL_BLANK, NULL_BLANK, DECIMAL_PRICE
from management.apps.customers.models import Customer
from management.apps.orders.choices import OrderTypeChoices


class Photo(AbstractModelController):
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return f'Photo <{self.id}>'


class Order(AbstractSoftDeletionModelController):
    choices = OrderTypeChoices()

    subject = models.CharField(**CHAR_NULL_BLANK)
    note = models.TextField(**NULL_BLANK)
    start_date = models.DateField(**NULL_BLANK)
    type = models.CharField(
        choices=OrderTypeChoices.TYPE_CHOICE,
        default=OrderTypeChoices.LIP,
        max_length=20
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    total_price = models.DecimalField(**DECIMAL_PRICE)

    def __str__(self):
        return f'Order <{self.id}>'


class OrderDetail(AbstractSoftDeletionModelController):
    detail = models.TextField(**NULL_BLANK)
    photo = models.ManyToManyField(
        Photo,
        blank=True
    )
    price = models.DecimalField(**DECIMAL_PRICE)
    date = models.DateField(**NULL_BLANK)
    sequence = models.IntegerField(**NULL_BLANK, default=0)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='details'
    )

    def __str__(self):
        return f'Detail <{self.id}>'

