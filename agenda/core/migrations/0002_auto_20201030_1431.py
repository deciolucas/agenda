# Generated by Django 3.1.2 on 2020-10-30 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='data_evento',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='local_evento',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='titulo',
        ),
        migrations.AlterModelTable(
            name='evento',
            table=None,
        ),
    ]
