# Generated by Django 5.0 on 2024-12-23 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_calculator', '0011_remove_materialusage_tasks_task_materialusage_task_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='estimated_hours',
        ),
        migrations.AlterField(
            model_name='task',
            name='house_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cost_calculator.housepart'),
        ),
    ]
