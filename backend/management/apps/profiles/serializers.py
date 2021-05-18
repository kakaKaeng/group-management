from model_controller.serializers import ModelControllerSerializer
from rest_framework import serializers

from management.apps.commons.constants import EXCLUDE_COMMON_FIELDS
from management.apps.commons.serializers import UserSerializer
from management.apps.profiles.models import Profile


class ProfileSerializer(ModelControllerSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileMeSerializer(serializers.Serializer):
    user = UserSerializer()



    class Meta:
        model = Profile
        exclude = EXCLUDE_COMMON_FIELDS
