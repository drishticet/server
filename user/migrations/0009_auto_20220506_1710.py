# Generated by Django 3.1.14 on 2022-05-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20220506_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]