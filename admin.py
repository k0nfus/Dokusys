from django.contrib import admin

from .models import Klient, Eintrag

class KlientAdmin(admin.ModelAdmin):
    list_display = ("name", "vorname", "telefonnummer","projekt",)
    search_fields = ("name", "vorname", "telefonnummer","projekt",)

class EintragAdmin(admin.ModelAdmin):
    list_display = ("klient", "datum", "doku",)
    search_fields = ("klient", "datum", "doku",)

admin.site.register(Klient, KlientAdmin)
admin.site.register(Eintrag, EintragAdmin)