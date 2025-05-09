from django.contrib.auth.models import User 
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
     repeated_password=serializers.CharField(write_only=True)
     privacy_policy = serializers.BooleanField(write_only=True)
     class Meta:
         model=User  
         fields=['username','email','password','repeated_password','privacy_policy']
         extra_kwargs = {
            'password': {'write_only': True},
        }
         

     def save(self):
          pw=self.validated_data['password']
          repeated_password=self.validated_data['repeated_password']         
          privacy=self.validated_data['privacy_policy']

          if privacy!=True:
              raise serializers.ValidationError({'error:''Please '})
          elif pw!=repeated_password:
              raise serializers.ValidationError({'error:''password not corect'})
          account=User(email=self.validated_data['email'],username=self.validated_data['username'])
          #set_password(pw) ist wichtig: Dadurch wird das Passwort verschlüsselt gespeichert (nicht im Klartext!).
          account.set_password(pw)
          account.save()
          return account 


