from xml.parsers.expat import model
from rest_framework import serializers
from.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields ='__all__'