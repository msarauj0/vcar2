from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('placa', models.CharField(max_length=100, verbose_name='Placa')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('ano', models.CharField(max_length=7, verbose_name='Ano')),
                ('alugar', models.DateField(verbose_name='Data de aluguel')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='CPF')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('codigo', models.CharField(max_length=100, verbose_name='Codigo')),
                ('data_aluguel', models.DateField(verbose_name='Data de aluguel')),
                ('data_devolucao', models.DateField(verbose_name='Data de devolução')),
                ('diaria', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Diaria')),
            ],
        ),
    ]