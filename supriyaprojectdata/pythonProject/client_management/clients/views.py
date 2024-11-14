from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Client, Project
from .serializers import (
    ClientSerializer,
    ClientCreateSerializer,
    ProjectSerializer,
    ProjectCreateSerializer
)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ClientCreateSerializer
        return ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProjectListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        return ProjectSerializer

    def perform_create(self, serializer):
        client_id = self.request.data.get("client_id")
        client = Client.objects.get(id=client_id)
        serializer.save(created_by=self.request.user, client=client)

class ProjectDetailView(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

