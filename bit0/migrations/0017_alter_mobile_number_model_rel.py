# Generated by Django 3.2.8 on 2021-12-29 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bit0', '0016_alter_mobile_number_model_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile_number_model',
            name='rel',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
