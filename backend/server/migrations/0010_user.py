# Generated by Django 2.0 on 2019-12-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_auto_20191201_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USEREMAIL', models.CharField(max_length=100)),
                ('STUDENT_NUMBER', models.IntegerField(default=0)),
                ('TRACK', models.CharField(default='N', max_length=20)),
            ],
        ),
    ]
