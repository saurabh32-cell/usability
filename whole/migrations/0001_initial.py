# Generated by Django 3.1.6 on 2021-03-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/uploads')),
            ],
        ),
    ]
