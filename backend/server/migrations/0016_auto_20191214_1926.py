# Generated by Django 2.0 on 2019-12-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0015_globalswcononsubject_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='gr',
            name='CATEGORY',
            field=models.CharField(default='N', max_length=100),
        ),
        migrations.AlterField(
            model_name='gr',
            name='CONTENT',
            field=models.CharField(default='N', max_length=100),
        ),
    ]