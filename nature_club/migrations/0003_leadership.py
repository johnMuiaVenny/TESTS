# Generated by Django 3.2.5 on 2021-07-04 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nature_club', '0002_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Images', models.FileField(upload_to='events')),
            ],
        ),
    ]