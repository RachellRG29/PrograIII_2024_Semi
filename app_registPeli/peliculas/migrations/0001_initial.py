# Generated by Django 5.1.2 on 2024-10-15 20:37

import peliculas.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_id', models.CharField(default=peliculas.models.generate_unique_id, editable=False, max_length=6, unique=True)),
                ('imagen', models.ImageField(upload_to='peliculas/')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(max_length=100)),
                ('clasificacion', models.CharField(max_length=10)),
                ('fecha_estreno', models.DateField()),
                ('director', models.CharField(max_length=100)),
                ('duracion', models.IntegerField()),
                ('idioma', models.CharField(max_length=50)),
            ],
        ),
    ]
