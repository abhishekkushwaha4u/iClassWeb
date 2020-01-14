# Generated by Django 3.0.1 on 2020-01-11 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0013_auto_20200112_0044'),
        ('accounts', '0003_auto_20191227_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='QuizSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('attemptTime', models.DateTimeField(auto_now_add=True)),
                ('quizId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('quizId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='questionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
    ]