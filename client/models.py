from django.db import models

class Client(models.Model):
    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )
    nome = models.CharField(max_length=50, help_text='Somente o primeiro nome.')
    sobrenome = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='n° telefone celular')
    protocolo = models.CharField(max_length=52, null=True, blank=True)

    def __str__(self): 
        return self.nome
