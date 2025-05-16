from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User = get_user_model()

def check_email(request):
    email = request.GET.get('email')
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})       

#Create Registration
class RegistrationView(APIView):
   permission_classes=[AllowAny] 

   def post(self,request):
      serializer=RegistrationSerializer(data=request.data)
      data={}
      if serializer.is_valid():
       saved_account=serializer.save()
       token, created = Token.objects.get_or_create(user=saved_account)
       data={
               "token":token.key,
               "username":saved_account.username,
               "email":saved_account.email
                }
       return Response(data)
      else:
        return  Response(serializer.errors)
      
  
    
# class CustomLoginView(ObtainAuthToken):
#    permission_classes=[AllowAny]

#Create Login
class CustomLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username_or_email = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=username_or_email)
            username = user.username
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=400)

        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "username": user.username,
                "email": user.email
            })
        else:
            return Response({"error": "Invalid credentials"}, status=400)
       

