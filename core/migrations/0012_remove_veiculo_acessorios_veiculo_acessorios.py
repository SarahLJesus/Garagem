# Generated by Django 5.1.7 on 2025-04-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_veiculo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='acessorios',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='acessorios',
            field=models.ManyToManyField(blank=True, null=True, related_name='acessorio', to='core.acessorio'),
        ),
    ]
