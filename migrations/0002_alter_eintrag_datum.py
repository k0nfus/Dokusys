# Generated by Django 4.1.7 on 2023-03-12 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dokusys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eintrag',
            name='datum',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
