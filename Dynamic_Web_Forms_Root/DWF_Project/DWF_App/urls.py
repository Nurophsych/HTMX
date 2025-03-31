from django.urls import path
from .views import entry_list, add_entry

urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('add/', add_entry, name='add_entry'),
]
