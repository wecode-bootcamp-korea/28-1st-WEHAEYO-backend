# Generated by Django 4.0 on 2022-01-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
