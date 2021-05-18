from django.contrib.auth.models import User
from django.db import models

from management.apps.commons import managers
from management.apps.commons.managers import SoftDeleteManager


class AbstractTimeStampMarker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractModelController(AbstractTimeStampMarker):
    created_user = models.ForeignKey(User, related_name="%(class)s_created_user", verbose_name="Created User",
                                     on_delete=models.DO_NOTHING)
    updated_user = models.ForeignKey(User, related_name="%(class)s_updated_user", verbose_name="Updated User",
                                     on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    class Meta:
        abstract = True

    objects = SoftDeleteManager()
    objects_with_deleted = managers.SoftDeleteManager(deleted=True)

    is_deleted = models.BooleanField(null=False, default=False)

    def delete(self, **kwargs):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()


class AbstractSoftModelController(SoftDeleteModel, AbstractModelController):
    """
    Shortcut for mixing Soft Delete and Model Controller
    """

    class Meta:
        abstract = True
