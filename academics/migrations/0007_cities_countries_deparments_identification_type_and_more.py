# Generated by Django 5.0.2 on 2024-03-16 05:14

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0006_remove_user_create_at_remove_user_deleted_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deparments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Identification_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('ident_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 194682))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 163477)),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 0, 14, 25, 163477)),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AddField(
            model_name='cities',
            name='id_dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.deparments'),
        ),
        migrations.AddField(
            model_name='persons',
            name='id_exp_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.cities'),
        ),
        migrations.AddField(
            model_name='persons',
            name='id_ident_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.identification_type'),
        ),
        migrations.AddField(
            model_name='persons',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.user'),
        ),
        migrations.AddField(
            model_name='students',
            name='id_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.persons'),
        ),
    ]
