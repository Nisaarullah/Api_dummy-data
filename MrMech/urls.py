from django.urls import path
from .views import CategoryList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    # Add more URLs for other views if needed
]
