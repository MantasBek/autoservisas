# Generated by Django 4.2.7 on 2023-11-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0006_automobilis_nuotrauka_alter_uzsakymas_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobilis',
            name='nuotrauka',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Mašina'),
        ),
    ]