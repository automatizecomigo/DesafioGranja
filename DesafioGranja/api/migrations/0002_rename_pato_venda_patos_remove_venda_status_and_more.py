# Generated by Django 5.1.1 on 2024-10-04 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='pato',
            new_name='patos',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='status',
        ),
        migrations.AddField(
            model_name='pato',
            name='filhos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pato',
            name='mae',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.pato'),
        ),
    ]
