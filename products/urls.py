from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    # category is a parameter passed to the views.category function
    path('category/<int:category_id>/', views.category, name="category"),
    path('product/<int:product_id>', views.product, name="product"),
    
]
