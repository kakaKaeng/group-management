from django.core.management import BaseCommand
from django.db import transaction

from management.apps.profiles.choices import RoleProfile
from management.apps.profiles.functions import create_user


class Command(BaseCommand):
    help = 'Initial DB'

    def handle(self, *args, **options):
        with transaction.atomic():
            create_user(
                username='admin',
                first_name='pattarapong',
                last_name='tantikoit',
                email='kakakaeng@gmail.com',
                password='freedom111i',
                role=RoleProfile.ADMIN)
