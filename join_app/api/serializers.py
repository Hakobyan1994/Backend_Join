from rest_framework import serializers
from join_app.models import CreateContacts,CreateTasks

class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContacts
        fields = '__all__'


class  CreateTasksSerializer(serializers.ModelSerializer):
   assignedTo = CreateContactSerializer(read_only=True, many=True)
   

   assignedTo_ids=serializers.PrimaryKeyRelatedField(
        queryset=CreateContacts.objects.all(), 
        many=True,
        write_only=True,
        source='assignedTo'
   ) 

   class Meta:
      model=CreateTasks
      fields = [
            'id', 'title', 'description',
            'assignedTo', 'assignedTo_ids',
            'date', 'prio', 'category', 'subtasks','status','checkoffs'
        ]
