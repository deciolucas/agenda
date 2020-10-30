from django.db import models

# Criando os modelos da minha agenda.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    local_evento = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo