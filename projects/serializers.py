from rest_framework import serializers

from .models import ProjectModel

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )