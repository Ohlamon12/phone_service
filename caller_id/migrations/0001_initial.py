# Generated by Django 2.2.7 on 2019-11-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone_number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SmallIntegerField()),
                ('start_number', models.IntegerField()),
                ('end_number', models.IntegerField()),
                ('company', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
            ],
        ),
    ]