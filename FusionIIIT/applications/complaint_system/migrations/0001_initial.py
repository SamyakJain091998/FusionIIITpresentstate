# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('hall-1', 'hall-1'), ('hall-3', 'hall-3'), ('hall-4', 'hall-4'), ('CC1', 'CC1'), ('CC2', 'CC2'), ('core_lab', 'core_lab'), ('LHTC', 'LHTC'), ('NR2', 'NR2'), ('Rewa_Residency', 'Rewa_Residency')], default='hall-3', max_length=20)),
                ('rating', models.IntegerField(default=0)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='StudentComplain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('complaint_finish', models.DateField(blank=True, null=True)),
                ('complaint_type', models.CharField(choices=[('Electricity', 'Electricity'), ('carpenter', 'carpenter'), ('plumber', 'plumber'), ('garbage', 'garbage'), ('dustbin', 'dustbin'), ('internet', 'internet'), ('other', 'other')], default='internet', max_length=20)),
                ('location', models.CharField(choices=[('hall-1', 'hall-1'), ('hall-3', 'hall-3'), ('hall-4', 'hall-4'), ('CC1', 'CC1'), ('CC2', 'CC2'), ('core_lab', 'core_lab'), ('LHTC', 'LHTC'), ('NR2', 'NR2'), ('Rewa_Residency', 'Rewa_Residency')], max_length=20)),
                ('specific_location', models.CharField(blank=True, max_length=50)),
                ('details', models.CharField(max_length=100)),
                ('status', models.IntegerField(default='0')),
                ('remarks', models.CharField(default='Pending', max_length=300)),
                ('flag', models.IntegerField(default='0')),
                ('reason', models.CharField(blank=True, max_length=100)),
                ('feedback', models.CharField(blank=True, max_length=500)),
                ('complainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('hall-1', 'hall-1'), ('hall-3', 'hall-3'), ('hall-4', 'hall-4'), ('CC1', 'CC1'), ('CC2', 'CC2'), ('core_lab', 'core_lab'), ('LHTC', 'LHTC'), ('NR2', 'NR2'), ('Rewa_Residency', 'Rewa_Residency')], max_length=20)),
                ('sup_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=10)),
                ('phone', models.IntegerField(blank=True)),
                ('worker_type', models.CharField(choices=[('Electricity', 'Electricity'), ('carpenter', 'carpenter'), ('plumber', 'plumber'), ('garbage', 'garbage'), ('dustbin', 'dustbin'), ('internet', 'internet'), ('other', 'other')], default='internet', max_length=20)),
                ('caretaker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint_system.Caretaker')),
            ],
        ),
        migrations.AddField(
            model_name='studentcomplain',
            name='worker_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complaint_system.Workers'),
        ),
    ]
