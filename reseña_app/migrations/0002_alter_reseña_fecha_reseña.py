# Generated by Django 5.1.2 on 2024-11-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reseña_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseña',
            name='fecha_reseña',
            field=models.CharField(max_length=100),
        ),
    ]
