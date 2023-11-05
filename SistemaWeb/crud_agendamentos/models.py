from django.db import models
from django.urls import reverse
from crud_medicos.models import Doctor
from crud_pacientes.models import Patient

class Agendamento(models.Model):
    STATUS_CHOICES = (
        ('A Confirmar', 'A Confirmar'),
        ('Confirmado', 'Confirmado'),
        ('Finalizado', 'Finalizado'),
    )

    Data = models.DateTimeField()
    Descricao = models.TextField()
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    Medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('agendamento_detail', args=[str(self.id)])
