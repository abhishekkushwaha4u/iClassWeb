# Generated by Django 3.0.1 on 2020-01-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0010_auto_20200110_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassignmentsubmission',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
