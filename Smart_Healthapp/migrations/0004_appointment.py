# Generated by Django 5.1.2 on 2024-11-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smart_Healthapp', '0003_alter_product_serial_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('date', models.DateTimeField()),
                ('department', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
    ]
