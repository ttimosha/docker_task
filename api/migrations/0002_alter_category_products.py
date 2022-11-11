# Generated by Django 3.2.16 on 2022-11-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='categories', through='api.ProductCategory', to='api.Product'),
        ),
    ]