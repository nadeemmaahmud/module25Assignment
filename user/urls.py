from django.urls import path
from . views import logout_view, login_view, register_view, edit_profile_view
urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', edit_profile_view, name='profile'),
]