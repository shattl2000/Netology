# Generated by Django 2.1.1 on 2019-05-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20190521_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player1_result_viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='player2_result_viewed',
            field=models.BooleanField(default=False),
        ),
    ]