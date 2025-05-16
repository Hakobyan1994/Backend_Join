from rest_framework import serializers
from join_app.models import CreateContacts,CreateTasks



# 🔹 Serializer for the CreateContacts model
# Automatically maps all model fields to serializer fields
# Used for serializing/deserializing contact data in API requests and responses
class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContacts     # The model this serializer is based on
        fields = '__all__'         # Includes all fields from the model 


#  Serializer for the CreateTasks model
# Handles both read and write logic for assigned contacts and other task fields
class  CreateTasksSerializer(serializers.ModelSerializer):
    #  Write-only field to assign contacts by their IDs
    # This replaces the 'assignedTo' relation when creating/updating tasks
   assignedTo = CreateContactSerializer(read_only=True, many=True)
   assignedTo_ids=serializers.PrimaryKeyRelatedField(
        queryset=CreateContacts.objects.all(), 
        many=True,
        write_only=True,
        source='assignedTo'
   ) 

   class Meta:
      model=CreateTasks     # The model this serializer is based on
      # Includes all fields from the model 
      fields = [          
            'id', 'title', 'description',
            'assignedTo', 'assignedTo_ids',
            'date', 'prio', 'category', 'subtasks','status','checkoffs'
        ]
