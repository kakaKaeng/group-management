from django.contrib.auth.models import User

from management.apps.profiles.models import Profile


def create_user(username: str, first_name: str, last_name: str, email: str, password: str, role: str):
    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }
    )
    user.set_password(password)
    user.save()
    profile, created = Profile.objects.update_or_create(
        user=user,
        defaults={
            'role': role,
            'created_user': user,
            'updated_user': user
        }
    )
