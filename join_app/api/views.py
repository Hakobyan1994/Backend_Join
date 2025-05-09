from rest_framework import generics,status
from join_app.models import CreateContacts,CreateTasks
from .serializers import CreateContactSerializer,CreateTasksSerializer
from rest_framework.response import Response

class CreateContactList(generics.ListCreateAPIView):
    queryset = CreateContacts.objects.all()
    serializer_class = CreateContactSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Stelle sicher, dass du eine normale JSON-Antwort zurückgibst:
        return Response({'status': 'success', 'data': response.data}, status=status.HTTP_201_CREATED)



class CreateContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=CreateContacts.objects.all()
    serializer_class=CreateContactSerializer    

class CreateTasksList(generics.ListCreateAPIView):
    queryset=CreateTasks.objects.all()
    serializer_class=CreateTasksSerializer

class CreateTasksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=CreateTasks.objects.all()
    serializer_class=CreateTasksSerializer