# Generated by Django 4.2.5 on 2023-10-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('value', models.IntegerField()),
                ('country', models.CharField(max_length=40)),
            ],
        ),
    ]