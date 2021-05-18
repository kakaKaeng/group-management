from django.contrib.auth.models import User
from django.db import models
from model_controller.models import AbstractModelController

from management.apps.commons.constants import NULL_BLANK
from management.apps.commons.utils import RandomFileName
from management.apps.profiles.choices import RoleProfile


class Profile(AbstractModelController):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                **NULL_BLANK)
    photo = models.ImageField(
        upload_to=RandomFileName("profile/photo"),
        verbose_name='Photo',
        **NULL_BLANK
    )
    email = models.EmailField(**NULL_BLANK)
    role = models.CharField(choices=RoleProfile.ROLE_TYPE_CHOICES,
                            default=RoleProfile.GENERAL,
                            max_length=25)
