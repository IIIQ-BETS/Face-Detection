# Generated by Django 5.0.2 on 2024-04-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.TextField(),
        ),
    ]