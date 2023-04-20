from django.urls import path
from .views import ProductListAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDetailAPIView, ProductDeleteAPIView


urlpatterns = [
    path('all', ProductListAPIView.as_view(), name='all-product'),
    path('create/', ProductCreateAPIView.as_view(), name='create-product'),
    path('update/<int:id>/', ProductUpdateAPIView.as_view(), name='update-product'),
    path('<int:id>/', ProductDetailAPIView.as_view(), name='retrieve-product'),
    path('<int:id>/delete/', ProductDeleteAPIView.as_view(), name='delete-product'),



    ]