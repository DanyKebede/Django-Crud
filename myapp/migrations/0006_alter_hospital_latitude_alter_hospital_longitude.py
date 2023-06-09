# Generated by Django 4.2.1 on 2023-06-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_doctor_linkedin_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]
