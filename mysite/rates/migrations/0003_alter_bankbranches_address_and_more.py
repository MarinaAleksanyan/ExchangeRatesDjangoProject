# Generated by Django 4.1.5 on 2023-01-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_alter_bankbranches_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankbranches',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bankbranches',
            name='branch_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bankbranches',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bankbranches',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
