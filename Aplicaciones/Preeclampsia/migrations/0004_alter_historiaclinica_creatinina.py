# Generated by Django 5.0.6 on 2024-09-12 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preeclampsia', '0003_alter_historiaclinica_proteinaorina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='creatinina',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
