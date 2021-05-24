# Generated by Django 3.1.6 on 2021-05-24 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import model_controller.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('alive', model_controller.fields.LiveField(db_index=True, default=True, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(choices=[('lip', 'Lip'), ('lash', 'Lash')], default='lip', max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_created_user', to=settings.AUTH_USER_MODEL, verbose_name='Created User')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customers.customer')),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='Updated User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('image', models.ImageField(upload_to='photos')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_created_user', to=settings.AUTH_USER_MODEL, verbose_name='Created User')),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='Updated User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('alive', model_controller.fields.LiveField(db_index=True, default=True, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('date', models.DateField(blank=True, null=True)),
                ('sequence', models.IntegerField(blank=True, default=0, null=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdetail_created_user', to=settings.AUTH_USER_MODEL, verbose_name='Created User')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='orders.order')),
                ('photo', models.ManyToManyField(blank=True, to='orders.Photo')),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdetail_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='Updated User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]