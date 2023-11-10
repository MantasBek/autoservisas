from django.contrib import admin
from .models import Automobilis, Automobilio_modelis, Paslauga, Uzsakymas, Uzsakymo_eilute
# Register your models here.
class Uzsakymo_Eilute_Inline(admin.TabularInline):
    model = Uzsakymo_eilute
    extra = 0

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('id', 'klientas','display_automobilis', 'valstybinis_nr', 'vin_kodas')
    list_filter = ('klientas', 'automobilio_modelis_id__modelis')
    search_fields = ('valstybinis_nr', 'vin_kodas')
    search_help_text = ('Paieška pagal valstybinį Nr. ar VIN kodą')
class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('id', 'automobilis_id', 'data')
    inlines = [Uzsakymo_Eilute_Inline]

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')

admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Automobilio_modelis)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Uzsakymo_eilute)