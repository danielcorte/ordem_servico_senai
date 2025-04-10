# Generated by Django 5.1.5 on 2025-04-07 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=64)),
                ('responsavel', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gestores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=64)),
                ('area', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patrimonios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=255)),
                ('localizacao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manutentores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=64)),
                ('area', models.CharField(max_length=255)),
                ('gestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gestores')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridade', models.CharField(choices=[('alta', 'Alta'), ('media', 'Media'), ('baixa', 'Baixa')], max_length=5)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ambientes')),
                ('manutentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.manutentores')),
                ('patrimonio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patrimonios')),
            ],
        ),
    ]
