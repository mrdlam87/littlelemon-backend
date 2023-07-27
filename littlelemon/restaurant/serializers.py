from rest_framework import serializers
from .models import MenuItem, Category, Booking


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price',
                  'inventory', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory': {'min_value': 0}
        }


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
