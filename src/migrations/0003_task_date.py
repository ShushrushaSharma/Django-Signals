# Generated by Django 5.1.1 on 2024-09-10 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_task_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.task')),
            ],
        ),
    ]
