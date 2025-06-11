from rest_framework import serializers
from .models import Category, Product , Branch


class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'image','price','description']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'products']



class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'image','working_hours','address']