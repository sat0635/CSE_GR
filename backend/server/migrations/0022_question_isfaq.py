# Generated by Django 2.0 on 2019-12-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0021_user_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ISFAQ',
            field=models.BooleanField(default=False),
        ),
    ]
