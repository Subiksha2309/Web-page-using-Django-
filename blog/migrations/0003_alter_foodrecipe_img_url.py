# Generated by Django 5.1 on 2024-09-04 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_foodrecipe_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodrecipe',
            name='img_url',
            field=models.URLField(null=True),
        ),
    ]
