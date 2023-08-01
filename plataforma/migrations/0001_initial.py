# Generated by Django 4.2.3 on 2023-07-31 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DiasVisita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('quartos', models.IntegerField()),
                ('tamanho', models.FloatField()),
                ('rua', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('V', 'Venda'), ('A', 'Aluguel')], max_length=1)),
                ('tipo_imovel', models.CharField(choices=[('A', 'Apartamento'), ('C', 'Casa')], max_length=1)),
                ('numero', models.IntegerField()),
                ('descricao', models.TextField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plataforma.cidade')),
                ('dias_visita', models.ManyToManyField(to='plataforma.diasvisita')),
                ('horarios', models.ManyToManyField(to='plataforma.horario')),
                ('imagens', models.ManyToManyField(to='plataforma.imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=20)),
                ('horario', models.TimeField()),
                ('status', models.CharField(choices=[('A', 'Agendado'), ('F', 'Finalizado'), ('C', 'Cancelado')], default='A', max_length=1)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plataforma.imovel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
