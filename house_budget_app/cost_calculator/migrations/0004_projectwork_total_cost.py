# Generated by Django 5.0 on 2024-12-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_calculator', '0003_materialcategory_housepart_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectwork',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
