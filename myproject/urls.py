from django.contrib import admin
from django.urls import path, include
from items.views import ItemCreateView  # Import the view directly

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', ItemCreateView.as_view(), name='item-create'),  # Root URL now points to the API
]
