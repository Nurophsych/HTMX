from django.contrib import admin
from django.urls import include, path
from DWF_App.views import entry_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entry_list, name='entry_list'),  # Map the root URL to entry_list view
    path('entries/', include('DWF_App.urls')),  # Include the app URLs
]
