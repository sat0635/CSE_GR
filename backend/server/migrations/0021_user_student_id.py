# Generated by Django 2.0 on 2019-12-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0020_auto_20191215_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='STUDENT_ID',
            field=models.CharField(default='N', max_length=100),
        ),
    ]
