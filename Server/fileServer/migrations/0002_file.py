# Generated by Django 2.0.5 on 2018-05-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileServer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to='static')),
            ],
        ),
    ]