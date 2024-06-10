# Generated by Django 4.2.11 on 2024-06-08 22:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=500, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('studyField', models.CharField(max_length=200)),
                ('Experience', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=5000)),
                ('Organization_Name', models.CharField(max_length=500)),
                ('Organization_Email', models.EmailField(max_length=254, verbose_name='email address')),
                ('Organization_Description', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ymp_id',
        ),
        migrations.RemoveField(
            model_name='hourrecord',
            name='next_week_plans',
        ),
        migrations.RemoveField(
            model_name='hourrecord',
            name='teamlead_email',
        ),
        migrations.RemoveField(
            model_name='hourrecord',
            name='ymp_id',
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='customuser',
            name='userType',
            field=models.CharField(default='Student', max_length=200),
        ),
        migrations.AddField(
            model_name='hourrecord',
            name='Organizer_Email',
            field=models.EmailField(default='email@gmail.com', max_length=254, null=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='hourrecord',
            name='user_id',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='hourrecord',
            name='date',
            field=models.CharField(max_length=5000),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=5000, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=5000)),
                ('Event_Name', models.CharField(max_length=500)),
                ('Event_Description', models.CharField(max_length=2000)),
                ('Event_Location', models.CharField(max_length=2000)),
                ('Event_Time', models.CharField(max_length=2000)),
                ('participants', models.ManyToManyField(blank=True, related_name='events_participated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
