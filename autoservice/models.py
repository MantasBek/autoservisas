from django.db import models


# Create your models here.


class Paslauga(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite paslaugos pavadinimą')
    kaina = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

    def __str__(self):
        return self.pavadinimas


def validate_at_least_one_digit(value):
    if not any(char.isdigit() for char in value):
        raise ValueError('Neteisingai įvestas automobilio numeris.')

class Automobilis(models.Model):
    valstybinis_nr = models.CharField('Valstybinis_NR', max_length=6, validators=[validate_at_least_one_digit],
                                      help_text='Įvestas automobilio numeris turi turėti bent vieną skaičių.')
    automobilio_modelis_id = models.ForeignKey('Automobilio_modelis', on_delete=models.CASCADE)
    vin_kodas = models.CharField('VIN_kodas', max_length=17, help_text='Įveskite automobilio VIN kodą')
    klientas = models.CharField('Klientas', max_length=200, help_text='Įveskite aptarnaujamo žmogaus vardą pavardę')

    def display_automobilis(self):
        return f'{self.automobilio_modelis_id.marke}, {self.automobilio_modelis_id.modelis}'

    display_automobilis.short_description = 'Automobilis'

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

    def __str__(self):
        return f'{self.klientas}, Valstybinis Nr: {self.valstybinis_nr}'


class Automobilio_modelis(models.Model):
    marke = models.CharField('Markė', max_length=30)
    modelis = models.CharField('Modelis', max_length=50)

    class Meta:
        verbose_name = 'Automobilio_modelis'
        verbose_name_plural = 'Automobilio_modeliai'

    def __str__(self):
        return f'{self.marke}, {self.modelis}'


class Uzsakymas(models.Model):
    data = models.DateField('Uzsakymo_data')
    automobilis_id = models.ForeignKey('Automobilis', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

    SERVIZO_STATUSAS = (
        ('r', 'Rezervuota'),
        ('a', 'Atšaukta'),
        ('t', 'Atlikta'),
        ('v', 'Vykdoma'),
    )

    status = models.CharField(max_length=1, choices=SERVIZO_STATUSAS, help_text='Statusas')

    def __str__(self):
        return str(self.automobilis_id)


class Uzsakymo_eilute(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.CASCADE)
    uzsakymas_id = models.ForeignKey('Uzsakymas', on_delete=models.CASCADE)
    kiekis = models.PositiveIntegerField('Kiekis', help_text='Įveskite kiekį')

    class Meta:
        verbose_name = 'Užsakymo_lentelė'
        verbose_name_plural = 'Užsakymų_lentelė'

    def __str__(self):
        return f'{self.uzsakymas_id} Paslauga: {self.paslauga_id}'