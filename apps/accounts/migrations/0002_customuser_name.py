# Generated by Django 5.1.6 on 2025-02-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='Teste', max_length=150, verbose_name='Nome Completo'),
        ),
    ]
