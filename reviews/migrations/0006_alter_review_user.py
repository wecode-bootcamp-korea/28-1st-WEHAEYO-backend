# Generated by Django 4.0 on 2022-01-01 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_wishilists'),
        ('reviews', '0005_alter_menu_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user'),
        ),
    ]