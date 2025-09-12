# claims/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.claim_list_view, name='claim_list'),
    path('claim/<int:pk>/', views.claim_detail_view, name='claim_detail'),
    path('claim/<int:pk>/toggle-flag/', views.toggle_flag_view, name='toggle_flag'),
    path('claim/<int:pk>/add-note/', views.add_note_view, name='add_note'),
    path('note/<int:pk>/delete/', views.delete_note_view, name='delete_note'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]