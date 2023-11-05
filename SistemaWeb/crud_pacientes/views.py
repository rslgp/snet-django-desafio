from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient

from django.contrib.auth.mixins import LoginRequiredMixin #must be logged to access page

class PatientListView(LoginRequiredMixin, ListView): #login required
    model = Patient
    template_name = 'patient_list.html'
    context_object_name = 'patients'
    login_url = '/accounts/login/'

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient'
    login_url = '/accounts/login/'

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'patient_create.html'
    fields = ['Nome', 'Telefone', 'Endereco', 'Numero', 'Cidade', 'UF', 'Pais', 'CEP']
    success_url = reverse_lazy('patient_list')
    login_url = '/accounts/login/'

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = 'patient_update.html'
    fields = ['Nome', 'Telefone', 'Endereco', 'Numero', 'Cidade', 'UF', 'Pais', 'CEP']
    success_url = reverse_lazy('patient_list')
    login_url = '/accounts/login/'

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')
    login_url = '/accounts/login/'
