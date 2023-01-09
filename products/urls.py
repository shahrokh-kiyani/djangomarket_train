from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('<int:pk>/', detail_view, name="detail"),
]
