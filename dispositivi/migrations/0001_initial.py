# Generated by Django 2.0.4 on 2019-10-10 07:34

import dispositivi.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anagrafica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allegato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(blank=True, max_length=30, null=True)),
                ('allegato', models.FileField(upload_to='')),
                ('inserito_il', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'allegato',
                'verbose_name_plural': 'allegati',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(max_length=10, unique=True)),
                ('location', models.CharField(choices=[('Torino', 'Torino'), ('Milano', 'Milano'), ('Roma', 'Roma'), ('Amburgo', 'Amburgo'), ('Toronto', 'Toronto'), ('Pechino', 'Pechino')], default=('Torino', 'Torino'), max_length=30)),
                ('palazzo', models.CharField(blank=True, max_length=20, null=True)),
                ('piano', models.CharField(blank=True, max_length=10, null=True)),
                ('stanza', models.CharField(blank=True, max_length=3, null=True)),
                ('seriale', models.CharField(max_length=30, unique=True)),
                ('data_installazione', models.DateField(validators=[dispositivi.models.valida_data_installazione])),
                ('data_dismissione', models.DateField(blank=True, null=True, validators=[dispositivi.models.valida_data_dismissione])),
                ('fine_garanzia', models.DateField(blank=True, null=True)),
                ('os', models.CharField(blank=True, max_length=15, null=True, verbose_name='O.S')),
                ('note', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'dispositivi',
            },
        ),
        migrations.CreateModel(
            name='Modello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modello', models.CharField(max_length=30, unique=True)),
                ('attivo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'modello',
                'verbose_name_plural': 'modelli',
                'ordering': ['modello'],
            },
        ),
        migrations.CreateModel(
            name='Produttore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produttore', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'produttore',
                'verbose_name_plural': 'produttori',
                'ordering': ['produttore'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_dispositivo', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'dispositivo',
                'verbose_name_plural': 'tipi dispositivo',
                'ordering': ['tipo_dispositivo'],
            },
        ),
        migrations.AddField(
            model_name='modello',
            name='fk_produttore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivi.Produttore', verbose_name='produttore'),
        ),
        migrations.AddField(
            model_name='modello',
            name='fk_tipo_dispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivi.Tipo_Dispositivo', verbose_name='tipo dispositivo'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='modello',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivi.Modello', verbose_name='modello'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='produttore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivi.Produttore', verbose_name='produttore'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='tipo_dispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivi.Tipo_Dispositivo', verbose_name='tipo dispositivo'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='utente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anagrafica.Utente', verbose_name='assegnatario'),
        ),
        migrations.AddField(
            model_name='allegato',
            name='dispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivi.Dispositivo'),
        ),
    ]
