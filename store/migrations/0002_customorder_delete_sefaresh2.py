# Generated by Django 4.0.4 on 2022-07-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('message', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
