from rest_framework import serializers
from .models import Room
# converts the room models into a json res
class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields = ("__all__")
