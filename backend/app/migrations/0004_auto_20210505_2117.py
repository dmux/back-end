# Generated by Django 3.1.9 on 2021-05-05 21:17

from django.db import migrations
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210505_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='batch',
            field=encrypted_fields.fields.EncryptedCharField(blank=True, max_length=255, null=True, verbose_name='Lote'),
        ),
        migrations.AlterField(
            model_name='card',
            name='date',
            field=encrypted_fields.fields.EncryptedCharField(blank=True, max_length=255, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=encrypted_fields.fields.EncryptedCharField(blank=True, max_length=255, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='card',
            name='qty_records',
            field=encrypted_fields.fields.EncryptedCharField(blank=True, max_length=255, null=True, verbose_name='Qtd Registros'),
        ),
        migrations.AlterField(
            model_name='cardrow',
            name='batch',
            field=encrypted_fields.fields.EncryptedCharField(blank=True, max_length=255, null=True, verbose_name='Númeração do Lote'),
        ),
        migrations.AlterField(
            model_name='cardrow',
            name='number',
            field=encrypted_fields.fields.EncryptedCharField(blank=True, max_length=255, null=True, verbose_name='Número de Cartão Completo'),
        ),
        migrations.AlterField(
            model_name='cardrow',
            name='tag',
            field=encrypted_fields.fields.EncryptedCharField(blank=True, max_length=255, null=True, verbose_name='Identificador da Linha'),
        ),
    ]
