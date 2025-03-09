from .views import SignUpView
from django.urls import path, include

urlpatterns = [path('singup/', SignUpView.as_view(), name='signup'),
                ]