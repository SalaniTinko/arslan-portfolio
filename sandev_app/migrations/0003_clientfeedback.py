# Generated by Django 3.1.4 on 2020-12-23 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandev_app', '0002_auto_20201223_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('Country', models.CharField(blank=True, max_length=50)),
                ('feedback', models.TextField(blank=True)),
            ],
        ),
    ]
