# Generated by Django 4.2.1 on 2023-06-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybandblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age_member',
            field=models.IntegerField(),
        ),
    ]
