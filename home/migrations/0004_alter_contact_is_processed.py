# Generated by Django 4.0.3 on 2022-04-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_is_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_processed',
            field=models.BooleanField(blank=None, default=False, verbose_name='Обработан?'),
        ),
    ]
