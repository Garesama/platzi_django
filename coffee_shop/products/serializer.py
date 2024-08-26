from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'available',
            'photo',
            ]