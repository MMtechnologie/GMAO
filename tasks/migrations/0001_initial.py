# Generated by Django 4.1.6 on 2023-02-08 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Panne',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=150)),
                ('Time', models.CharField(default=django.utils.timezone.now, max_length=20)),
                ('state', models.CharField(max_length=10)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Curative',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=150)),
                ('timestop', models.TimeField()),
                ('panne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.panne')),
            ],
        ),
    ]
