# Generated by Django 3.0.1 on 2019-12-31 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20191227_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('classRoomId', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('roomNumber', models.IntegerField()),
                ('courseName', models.CharField(max_length=50, verbose_name='Course Name')),
                ('studentId', models.ManyToManyField(to='accounts.Student')),
                ('teacherId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=50)),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.ClassRoom')),
            ],
        ),
    ]