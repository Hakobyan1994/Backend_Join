from django.db import models

# Create your models here.
class CreateContacts(models.Model):
     name = models.CharField(max_length=100, blank=False, null=False)
     email = models.EmailField(blank=False, null=False, unique=True)
     phone = models.CharField(max_length=20, blank=False, null=False)


class CreateTasks(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=1000,blank=True)    
    assignedTo = models.ManyToManyField('CreateContacts', related_name='tasks',blank=True)
    date = models.DateField(blank=False, null=False)
    prio = models.CharField(default='medium', max_length=20, blank=False, null=False)
    category = models.CharField(max_length=40, blank=False, null=False)
    subtasks = models.JSONField(blank=True,default=list)
    status = models.CharField(max_length=50, blank=False)     
    checkoffs=models.JSONField(blank=True,default=list)