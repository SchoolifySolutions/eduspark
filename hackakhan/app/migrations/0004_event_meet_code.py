# Generated by Django 4.2.11 on 2024-06-08 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Meet_Code',
            field=models.CharField(default='EO92RO', max_length=10),
            preserve_default=False,
        ),
    ]
