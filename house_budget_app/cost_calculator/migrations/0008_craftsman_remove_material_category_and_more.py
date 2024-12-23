# Generated by Django 5.0 on 2024-12-22 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_calculator', '0007_remove_projectwork_total_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Craftsman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='material',
            name='category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.RemoveField(
            model_name='projectwork',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectwork',
            name='work',
        ),
        migrations.RemoveField(
            model_name='material',
            name='house_part',
        ),
        migrations.RemoveField(
            model_name='material',
            name='material_type',
        ),
        migrations.AlterField(
            model_name='housepart',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AlterField(
            model_name='housepart',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='material',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='material',
            name='unit',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('estimated_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('labor_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('craftsman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cost_calculator.craftsman')),
                ('house_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='cost_calculator.housepart')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost_calculator.material')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='cost_calculator.task')),
            ],
        ),
        migrations.DeleteModel(
            name='MaterialCategory',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectWork',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
