from rest_framework.viewsets import ModelViewSet

from management.apps.commons.permissions import IsAdminAuthenticated
from management.apps.customers.models import Customer
from management.apps.customers.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    permission_classes = [IsAdminAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.order_by('-id')

