from model_controller.serializers import ModelControllerSerializer
from rest_framework import serializers

from management.apps.commons.constants import EXCLUDE_COMMON_FIELDS
from management.apps.commons.serializers import UserSerializer
from management.apps.profiles.models import Profile


class ProfileSerializer(ModelControllerSerializer):
    full_name = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        exclude = EXCLUDE_COMMON_FIELDS


class ProfileMeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        exclude = EXCLUDE_COMMON_FIELDS
