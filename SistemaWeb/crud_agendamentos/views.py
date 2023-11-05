from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Agendamento
from .forms import AgendamentoForm

from crud_medicos.models import Doctor
from crud_pacientes.models import Patient

from django.contrib.auth.mixins import LoginRequiredMixin #must be logged to access page

class AgendamentoListView(LoginRequiredMixin, ListView):
    model = Agendamento
    template_name = 'agendamento_list.html'
    context_object_name = 'agendamentos'
    login_url = '/accounts/login/'

class AgendamentoDetailView(LoginRequiredMixin, DetailView):
    model = Agendamento
    template_name = 'agendamento_detail.html'
    context_object_name = 'agendamento'
    login_url = '/accounts/login/'

class AgendamentoCreateView(LoginRequiredMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamento_create.html'
    success_url = reverse_lazy('agendamento_list')
    login_url = '/accounts/login/'

    #se quiser usar template com design customizavel remova o comentario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        context['patients'] = Patient.objects.all()
        return context

class AgendamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Agendamento
    template_name = 'agendamento_create.html'
    fields = ['Data', 'Descricao', 'Status', 'Medico', 'Paciente']
    success_url = reverse_lazy('agendamento_list')
    login_url = '/accounts/login/'

    #se quiser usar template com design customizavel remova o comentario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        context['patients'] = Patient.objects.all()
        return context

class AgendamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Agendamento
    template_name = 'agendamento_confirm_delete.html'
    success_url = reverse_lazy('agendamento_list')
    login_url = '/accounts/login/'
