# Generated by Django 4.0.5 on 2022-07-03 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_receta_image_receta_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receta',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
    ]
