from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doctor

from django.contrib.auth.mixins import LoginRequiredMixin #must be logged to access page

class DoctorListView(LoginRequiredMixin, ListView): #login required
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'
    login_url = '/accounts/login/'

class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'
    context_object_name = 'doctor'
    login_url = '/accounts/login/'

class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    template_name = 'doctor_create.html'
    fields = ['Nome', 'E_mail', 'Senha']
    success_url = reverse_lazy('doctor_list')
    login_url = '/accounts/login/'

class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    template_name = 'doctor_update.html'
    fields = ['Nome', 'E_mail', 'Senha']
    success_url = reverse_lazy('doctor_list')
    login_url = '/accounts/login/'

class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'doctor_confirm_delete.html'
    success_url = reverse_lazy('doctor_list')
    login_url = '/accounts/login/'
