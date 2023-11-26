from rest_framework import viewsets, permissions

from .models import ProjectModel
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer