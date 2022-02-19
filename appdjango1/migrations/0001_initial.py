# Generated by Django 4.0.2 on 2022-02-16 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateField()),
                ('cidade_natal', models.CharField(max_length=200)),
            ],
        ),
    ]
