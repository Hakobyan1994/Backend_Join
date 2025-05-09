from django.urls import path
from .views import RegistrationView,CustomLoginView
from . import views

urlpatterns = [
    path('registration/',RegistrationView.as_view(),name="registration"),
    path('login/',CustomLoginView.as_view(),name="login"),
    path('check_email/', views.check_email, name="check_email"),
]