# Generated by Django 4.1 on 2022-08-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('courseID', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]
