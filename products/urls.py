from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # category is a parameter passed to the views.category function
    path('<str:category>/', views.category, name="category"),
    path('<str:category>/<str:product>', views.product),
]
