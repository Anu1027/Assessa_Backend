from django.urls import path
from .views import signup, LoginView
from .views import index  # Import the index view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('', index , name='home'),  # Route the root URL to your React app
]