# Generated by Django 3.1.3 on 2021-01-13 09:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seok', '0006_auto_20210113_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='hit',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
