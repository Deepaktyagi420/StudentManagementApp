# Generated by Django 4.2.4 on 2024-12-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='percentage',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
    ]
