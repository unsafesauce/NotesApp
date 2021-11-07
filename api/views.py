from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Note, Task
from django.contrib.auth.models import User
from .serializers import TaskSerializer, NoteSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['POST', 'PUT'])
    def text_note(self, request, pk=None):
        if 'text' in request.data:
            note = Note.objects.get(id=pk)
            text = request.data['text']
            title = request.data['title']
            user = request.user

            try:
                note = Note.objects.get(user=user.id, note=note.id)
                note.text = text
                text.save()
                serializers = NoteSerializer(text, many=False)
                return Response(status=status.HTTP_200_OK)

            except:
                note = Note.objects.create(user=user, text=text, title=title)
                serializer = NoteSerializer(note, Many=False)
                response = {'message': 'note already exists'}
                return Response(response, status=status.HTTP_208_ALREADY_REPORTED)
        else:
            response = {'message': 'You need to provide a text'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)