# Generated by Django 5.0.4 on 2024-05-14 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_gamers_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamers',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gamers',
            name='best_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best_players', to='account.games'),
        ),
    ]