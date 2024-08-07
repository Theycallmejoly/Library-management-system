from rest_framework import serializers
from .models import Book , Borrow


class BookSerializers(serializers.Modelserializer):
    class Meta:
        model = Book
        fields = '__all__'



class BorrowSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Borrow
        fields = '__all__'
        read_only_fields = ('borrow_date')  