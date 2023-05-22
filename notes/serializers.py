from rest_framework import serializers
from .models import Folder, Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'folder', 'tags', 'date', 'author']

class FolderSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ['id', 'title', 'notes']