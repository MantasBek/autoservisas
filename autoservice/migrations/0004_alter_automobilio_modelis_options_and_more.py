# Generated by Django 4.2.7 on 2023-11-09 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0003_uzsakymo_eilute'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobilio_modelis',
            options={'verbose_name': 'Automobilio_modelis', 'verbose_name_plural': 'Automobilio_modeliai'},
        ),
        migrations.AlterModelOptions(
            name='automobilis',
            options={'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AlterModelOptions(
            name='paslauga',
            options={'verbose_name': 'Paslauga', 'verbose_name_plural': 'Paslaugos'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymas',
            options={'verbose_name': 'Užsakymas', 'verbose_name_plural': 'Užsakymai'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymo_eilute',
            options={'verbose_name': 'Užsakymo_lentelė', 'verbose_name_plural': 'Užsakymų_lentelė'},
        ),
        migrations.RemoveField(
            model_name='uzsakymas',
            name='paslauga',
        ),
        migrations.AlterField(
            model_name='automobilis',
            name='automobilio_modelis_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='autoservice.automobilio_modelis'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uzsakymas',
            name='automobilis_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoservice.automobilis'),
        ),
        migrations.AlterField(
            model_name='uzsakymas',
            name='data',
            field=models.DateField(verbose_name='Uzsakymo_data'),
        ),
        migrations.AlterField(
            model_name='uzsakymo_eilute',
            name='paslauga_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='autoservice.paslauga'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uzsakymo_eilute',
            name='uzsakymas_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='autoservice.uzsakymas'),
            preserve_default=False,
        ),
    ]
