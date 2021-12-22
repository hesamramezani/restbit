# Generated by Django 3.2.8 on 2021-12-22 17:12

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bit0', '0007_mobile_number_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile_number_model',
            name='rel',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bit0.crypto_model'),
        ),
        migrations.AlterField(
            model_name='mobile_number_model',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]