from django.urls import path
from .views import RegisterAPI, LoginAPI, LogoutAPI, UpdateProfileAPI, DeleteAccountAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('update-profile/', UpdateProfileAPI.as_view(), name='update_profile'),
    path('delete-account/', DeleteAccountAPI.as_view(), name='delete_account'),
]