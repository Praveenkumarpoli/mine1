from django.urls import path
from .views import ItemCreateView

urlpatterns = [
    path('items/', ItemCreateView.as_view(), name='item-create'),  # API endpoint to create items
]
