from rest_framework import serializers 
from models import Specification, Customer, Cart, CartProduct, Product, Category


class SpecificationSerializers():
    class Meta():
        model = Specification
        fields = ('__all__')
    

class CustomerSerializers():
    class Meta():
        model = Customer
        fields = ('__all__')

class CartSerializers():
    class Meta():
        model = Cart
        fields = ('__all__')

class CartProductSerializers():
    class Meta():
        model = Cart
        fields = ('__all__')
    
class ProductSerilizers():
    class Meta():
        model = Product
        fields = ('__all__')


class CategorySerializers():
    class Meta():
        model = Category
        fields = ('__all__')

