# Generated by Django 2.0 on 2019-12-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_auto_20191214_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='cseintencosubject',
            name='ISESSENTIAL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='globalswcosubject',
            name='ISDESIGN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='globalswcosubject',
            name='ISESSENTIAL',
            field=models.BooleanField(default=False),
        ),
    ]