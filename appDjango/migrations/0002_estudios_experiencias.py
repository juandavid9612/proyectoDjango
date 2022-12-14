# Generated by Django 4.1.1 on 2022-09-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('estudio', models.CharField(max_length=50)),
                ('institucion', models.CharField(max_length=50)),
                ('tituloObtenido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('empresa', models.CharField(max_length=50)),
                ('jefeInmediato', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('responsabilidades', models.CharField(max_length=50)),
                ('logrosRealizados', models.CharField(max_length=50)),
            ],
        ),
    ]
