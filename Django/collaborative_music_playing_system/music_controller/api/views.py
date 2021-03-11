from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializers, CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your endpoints here


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    # api view allows to overide the request methods

    # post request for when a host is trying to create a room 
    def post(self, request, format=None):
        # checking and creating sessions 
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        # create a room using the request and CreateRoomSerializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # If the data is correct then create the room 
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            # check if the host already created a room
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            # If it does, then update the same room
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
            else:
            # create a new room 
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
        # .data to return data, but we could check the setting 
        return Response(RoomSerializers(room).data, status=status.HTTP_200_OK)
