# Generated by Django 5.0.1 on 2024-01-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=30)),
                ('cus_username', models.CharField(max_length=30)),
                ('cus_address', models.CharField(max_length=30)),
                ('cus_id', models.FileField(max_length=2000, upload_to='uploads/')),
                ('cus_pass', models.CharField(max_length=30)),
                ('cus_cpass', models.CharField(max_length=30)),
            ],
        ),
    ]
