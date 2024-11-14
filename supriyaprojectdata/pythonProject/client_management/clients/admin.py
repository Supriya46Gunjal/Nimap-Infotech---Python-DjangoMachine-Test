from django.contrib import admin
from .models import Client, Project

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'created_at')
    search_fields = ('client_name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'client', 'created_at')
    list_filter = ('client',)
    search_fields = ('project_name',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
