# Generated by Django 5.1.6 on 2025-03-24 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('authorName', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('addedOnDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedOnDate', models.DateTimeField(auto_now=True)),
                ('genre', models.CharField(choices=[('Self Help', 'Self Help'), ('Technology', 'Technology'), ('Humanities', 'Humanities'), ('Literature', 'Literature')], max_length=100)),
                ('authorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
    ]
