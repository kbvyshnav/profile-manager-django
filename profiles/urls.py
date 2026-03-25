from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-profile/', views.add_profile, name='add_profile'),
    path('update-profile/<int:id>', views.update_profile, name='update_profile'),
    path('delete-profile/<int:id>/', views.delete_profile, name='delete_profile'),
]