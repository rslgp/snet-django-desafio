from django.db import models
from django.utils import timezone

class Doctor(models.Model):
    Nome = models.CharField(max_length=255)
    E_mail = models.CharField(max_length=100)
    Senha = models.CharField(max_length=100)
    Data_de_Criacao = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.Data_de_Criacao = timezone.now() - timezone.timedelta(hours=3) #use GMT -3 Brazil
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Nome
    
    class Meta:
        app_label = 'crud_medicos'
