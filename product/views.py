from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)

from .models import Product
from .serializers import ProductSerializer
from user.permissions import IsOwnerOrReadOnly


class ProductListAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        return qs


class ProductCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductDetailAPIView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


