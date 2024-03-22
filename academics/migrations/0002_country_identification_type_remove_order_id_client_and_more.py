# Generated by Django 5.0.2 on 2024-03-22 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('abrebiation', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='identification_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('abrebiation', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='id_client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='id_product',
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('abrebiation', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.country')),
            ],
        ),
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('abrebiation', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.department')),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('id_ident_number', models.IntegerField(unique=True)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('id_ident_exp_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.cities')),
                ('id_ident_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.identification_type')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.user')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.person')),
            ],
        ),
        migrations.DeleteModel(
            name='client',
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='sale',
        ),
    ]
