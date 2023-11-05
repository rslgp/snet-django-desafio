from django import forms
from .models import Agendamento, Doctor, Patient
from django.utils import formats

class AgendamentoForm(forms.ModelForm):
    Data = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M'))
    
    class Meta:
        model = Agendamento
        fields = ['Data', 'Descricao', 'Status', 'Medico', 'Paciente']
        widgets = {
            'Data': forms.DateTimeInput(format='%d/%m/%Y %H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Medico'].queryset = Doctor.objects.all()
        self.fields['Paciente'].queryset = Patient.objects.all()
