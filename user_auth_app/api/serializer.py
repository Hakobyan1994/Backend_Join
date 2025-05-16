from django.contrib.auth.models import User 
from rest_framework import serializers



#Create registrationserializer
class RegistrationSerializer(serializers.ModelSerializer):
     username = serializers.CharField(validators=[], max_length=150)
     repeated_password=serializers.CharField(write_only=True)
     privacy_policy = serializers.BooleanField(write_only=True)
     class Meta:
         model=User  
         fields=['username','email','password','repeated_password','privacy_policy']
         extra_kwargs = {
            'password': {'write_only': True},
        }
         
    #Validating username
     def validate_username(self, value):
        if not value.strip():
            raise serializers.ValidationError("Username cannot be empty or only spaces.")
        return value    
     #creating function for saving user 
     def save(self):
          pw=self.validated_data['password']
          repeated_password=self.validated_data['repeated_password']         
          privacy=self.validated_data['privacy_policy']

          if privacy!=True:
              raise serializers.ValidationError({'error:''Please '})
          elif pw!=repeated_password:
              raise serializers.ValidationError({'error:''password not corect'})
          account=User(email=self.validated_data['email'],username=self.validated_data['username'])
          #set_password(pw) is important: This ensures that the password is stored encrypted (not in plain text!).
          account.set_password(pw)
          account.save()
          return account 


