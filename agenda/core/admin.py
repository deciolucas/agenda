from django.contrib import admin

from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo', 'data_evento',)

# Registrando as tabelas criadas.
admin.site.register(Evento, EventoAdmin)


