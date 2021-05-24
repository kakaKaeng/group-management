from model_controller.serializers import ModelControllerSerializer

from management.apps.commons.constants import EXCLUDE_COMMON_FIELDS
from management.apps.customers.models import Customer


class CustomerSerializer(ModelControllerSerializer):

    class Meta:
        model = Customer
        exclude = EXCLUDE_COMMON_FIELDS
