# Generated by Django 4.2.2 on 2023-07-12 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='comprado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='venda',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='venda',
            name='senha',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
