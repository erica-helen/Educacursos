# Generated by Django 4.2.2 on 2023-07-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_venda_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='senha',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
