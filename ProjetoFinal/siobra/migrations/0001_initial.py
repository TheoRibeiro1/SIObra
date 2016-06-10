# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-09 23:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('cidade_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('Tarefa_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('fornecedor_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('nome_logradouro', models.CharField(max_length=30)),
                ('complemento', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=8)),
                ('telefone', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=40)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('funcionario_id', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=45)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1)),
                ('estado_civil', models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divociado'), ('V', 'Viuvo'), ('O', 'Outro')], max_length=1)),
                ('naturalidade', models.CharField(max_length=45)),
                ('sangue_fator', models.CharField(max_length=2)),
                ('sangue_rh', models.CharField(max_length=1)),
                ('tipo_logradouro', models.CharField(choices=[('AVE', 'Avenida'), ('RUA', 'Rua'), ('PRA', 'Praça'), ('TRA', 'Travessa'), ('ROD', 'Rodovia'), ('VIL', 'Vila')], max_length=3)),
                ('nome_logradouro', models.CharField(max_length=30)),
                ('complemento', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=8)),
                ('telefone', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('admissao', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.CharField(max_length=40)),
                ('salario', models.FloatField(max_length=50)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('preco', models.FloatField()),
                ('qtd_estoque', models.IntegerField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('obra_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('tipo_logradouro', models.CharField(choices=[('AVE', 'Avenida'), ('RUA', 'Rua'), ('PRA', 'Praça'), ('TRA', 'Travessa'), ('ROD', 'Rodovia'), ('VIL', 'Vila')], max_length=3)),
                ('nome_logradouro', models.CharField(max_length=30)),
                ('complemento', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=8)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('progresso', models.TextField()),
                ('condicoes', models.TextField()),
                ('acidentes', models.TextField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Cidade')),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Equipamento')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Fornecedor')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Funcionario')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('pagamento_id', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.FloatField()),
                ('data_pagamento', models.DateTimeField(blank=True, null=True)),
                ('tipo_pagamento', models.CharField(choices=[('A', 'Avista'), ('T', 'Transferencia'), ('C', 'Cheque'), ('V', 'Vale')], max_length=1)),
                ('funcionario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('sigla', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('setor_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('sigla', models.CharField(max_length=10)),
                ('responsavel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('Tarefa_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('prazo', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('sigla', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Pais')),
            ],
        ),
        migrations.AddField(
            model_name='obra',
            name='pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Pagamento'),
        ),
        migrations.AddField(
            model_name='obra',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Setor'),
        ),
        migrations.AddField(
            model_name='obra',
            name='tarefa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Tarefa'),
        ),
        migrations.AddField(
            model_name='obra',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Uf'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='nacionalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Pais'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='tarefa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Tarefa'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Uf'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Uf'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Pais'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siobra.Uf'),
        ),
    ]