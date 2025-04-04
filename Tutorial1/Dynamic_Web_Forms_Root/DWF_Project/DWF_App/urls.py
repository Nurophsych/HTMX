from django.urls import path
from .views import entry_list, add_entry, edit_entry, delete_entry

urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('add/', add_entry, name='add_entry'),
    path('edit/<int:entry_id>/', edit_entry, name='edit_entry'),  # Edit entry URL
    path('delete/<int:entry_id>/', delete_entry, name='delete_entry'),  # Delete entry URL
]
