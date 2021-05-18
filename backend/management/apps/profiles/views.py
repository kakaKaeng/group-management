from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from management.apps.commons.permissions import IsAdminAuthenticated
from management.apps.profiles.models import Profile
from management.apps.profiles.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAdminAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('-id')

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        profile = request.user.profile  # type: Profile

        return Response('')

