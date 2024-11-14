from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
]
