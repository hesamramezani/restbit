# Generated by Django 3.2.8 on 2021-12-22 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bit0', '0008_auto_20211222_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile_number_model',
            name='rel',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bit0.crypto_model'),
        ),
    ]
