# Generated by Django 4.0.5 on 2022-07-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, default='empty.png', upload_to='portfolio')),
                ('description', models.TextField(null=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
