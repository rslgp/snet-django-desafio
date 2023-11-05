from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctor/detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor/delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
]
