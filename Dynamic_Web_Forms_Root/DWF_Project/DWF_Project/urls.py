from django.contrib import admin
from django.urls import include, path
from DWF_App.views import entry_list, add_entry  # ✅ Correct import from views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entry_list, name='entry_list'),
    path('add/', add_entry, name='add_entry'),
]
