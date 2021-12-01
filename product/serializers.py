from rest_framework import serializers
from product.models import Product
from category.models import Category

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'



