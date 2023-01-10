from django.urls import path

from .views import *


urlpatterns = [
    path("", cart_view, name="cart"),
    path("add/<int:product_id>/", add_to_cart_view, name="cart_add"),
    path("remove/<int:product_id>/", product_remove_view, name="cart_remove"),
]
