from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Patient(models.Model):    
    telefone_regex = RegexValidator(
        regex=r'^\(\d{2}\) \d{1}\d{4}-\d{4}$|^\(\d{2}\) \d{4}-\d{4}$',
        message="Telefone must be in the format '(##) #####-####' or '(##) ####-####'"
    )
    cep_regex = RegexValidator(
        regex=r'^\d{5}-\d{3}$',
        message="CEP must be in the format '#####-###'"
    )

    Nome = models.CharField(max_length=255)
    Endereco = models.CharField(max_length=255)
    Numero = models.CharField(max_length=10)
    Cidade = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)
    Pais = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=20, validators=[telefone_regex])
    CEP = models.CharField(max_length=10, validators=[cep_regex])
    Data_Criacao = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.Data_Criacao = timezone.now() - timezone.timedelta(hours=3) #use GMT -3 Brazil
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Nome
    
    class Meta:
        app_label = 'crud_pacientes'
