from django.urls import path
from .views import AgendamentoListView, AgendamentoDetailView, AgendamentoCreateView, AgendamentoUpdateView, AgendamentoDeleteView

urlpatterns = [
    path('agendamentos', AgendamentoListView.as_view(), name='agendamento_list'),
    path('agendamento/create/', AgendamentoCreateView.as_view(), name='agendamento_create'),
    path('agendamento/<int:pk>/', AgendamentoDetailView.as_view(), name='agendamento_detail'),
    path('agendamento/<int:pk>/update/', AgendamentoUpdateView.as_view(), name='agendamento_update'),
    path('agendamento/<int:pk>/delete/', AgendamentoDeleteView.as_view(), name='agendamento_delete'),
]
