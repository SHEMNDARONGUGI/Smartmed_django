# Generated by Django 5.1.2 on 2024-11-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smart_Healthapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serial_no', models.IntegerField()),
                ('price', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
