# Generated by Django 3.0.3 on 2020-03-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20200302_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='senha',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Indica que usuário consegue acessar este site de administração.', verbose_name='membro da equipe'),
        ),
    ]
