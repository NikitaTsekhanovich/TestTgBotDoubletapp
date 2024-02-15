from django.urls import path
from . import views


urlpatterns = [
    path('me/<int:user_id>', views.get_me)
]
