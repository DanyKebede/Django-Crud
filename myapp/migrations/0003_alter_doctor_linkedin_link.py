# Generated by Django 4.2.1 on 2023-06-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_doctor_image_alter_doctor_linkedin_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
