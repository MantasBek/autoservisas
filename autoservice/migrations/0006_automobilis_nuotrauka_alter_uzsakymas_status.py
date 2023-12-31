# Generated by Django 4.2.7 on 2023-11-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0005_uzsakymas_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilis',
            name='nuotrauka',
            field=models.ImageField(null=True, upload_to='nuotraukos', verbose_name='Mašina'),
        ),
        migrations.AlterField(
            model_name='uzsakymas',
            name='status',
            field=models.CharField(choices=[('r', 'Rezervuota'), ('a', 'Atšaukta'), ('t', 'Atlikta'), ('v', 'Vykdoma')], help_text='Statusas', max_length=1),
        ),
    ]
