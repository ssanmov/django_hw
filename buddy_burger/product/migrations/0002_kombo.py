# Generated by Django 4.0.5 on 2022-07-14 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kombo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, default='empty.png', upload_to='portfolio')),
                ('description', models.TextField(null=True)),
                ('price', models.IntegerField()),
                ('product_id_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_product', to='product.product')),
                ('product_id_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_product', to='product.product')),
            ],
        ),
    ]
