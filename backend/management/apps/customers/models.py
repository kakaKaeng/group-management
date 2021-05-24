from django.db import models
from model_controller.models import AbstractSoftDeletionModelController


class Customer(AbstractSoftDeletionModelController):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'Customer <{self.id}>'
