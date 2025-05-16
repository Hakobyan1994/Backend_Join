from rest_framework import generics,status
from join_app.models import CreateContacts,CreateTasks
from .serializers import CreateContactSerializer,CreateTasksSerializer
from rest_framework.response import Response


##  API View to list all contacts and create new ones for Contacts
# GET  -> returns a list of all contact entries
# POST -> creates a new contact entry
class CreateContactList(generics.ListCreateAPIView):
    queryset = CreateContacts.objects.all()
    serializer_class = CreateContactSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Stelle sicher, dass du eine normale JSON-Antwort zurückgibst:
        return Response({'status': 'success', 'data': response.data}, status=status.HTTP_201_CREATED)


#  API View to retrieve, update or delete a specific contact
# GET    -> returns a single contact by ID
# PUT    -> updates a contact completely
# PATCH  -> updates a contact partially
# DELETE -> deletes a contact by ID
class CreateContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=CreateContacts.objects.all()
    serializer_class=CreateContactSerializer    

##  API View to list all contacts and create new ones for Tasks
# GET  -> returns a list of all contact entries
# POST -> creates a new contact entry
class CreateTasksList(generics.ListCreateAPIView):
    queryset=CreateTasks.objects.all()
    serializer_class=CreateTasksSerializer
    
#  API View to retrieve, update or delete a specific contact
# GET    -> returns a single contact by ID
# PUT    -> updates a contact completely
# PATCH  -> updates a contact partially
# DELETE -> deletes a contact by ID
class CreateTasksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=CreateTasks.objects.all()
    serializer_class=CreateTasksSerializer