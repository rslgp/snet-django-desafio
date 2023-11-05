from django.urls import path
from .views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patient/detail/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patient/update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient/delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
]
