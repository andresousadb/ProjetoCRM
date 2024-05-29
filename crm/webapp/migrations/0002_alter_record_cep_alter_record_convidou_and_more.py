# Generated by Django 4.2 on 2024-03-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="cep",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="record",
            name="convidou",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="record",
            name="dt_nascimento",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="sexo",
            field=models.CharField(
                blank=True,
                choices=[("F", "Feminino"), ("M", "Masculino"), ("O", "Outros")],
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="record",
            name="status_civil",
            field=models.CharField(
                blank=True,
                choices=[
                    ("S", "Solteiro(a)"),
                    ("C", "Casado(a)"),
                    ("V", "Viúvo(a)"),
                    ("D", "Divorciado(a)"),
                    ("ND", "Não Declarar"),
                ],
                max_length=2,
            ),
        ),
    ]