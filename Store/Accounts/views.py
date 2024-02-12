# Import necessary modules and models
from ast import Not
from django.shortcuts import render, redirect
from .models import User, Customer, Seller
from .forms import registerform, seller_registerform, loginform
from django.http import JsonResponse
from rest_framework.response import Response

from .serializers import *
from rest_framework.decorators import action, permission_classes
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsCustomer,IsSeller
from rest_framework import permissions


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [IsCustomer]

    def get_serializer_class(self):
        if self.request.method=="POST":
            return CreateCustomerSerializer

        return CustomerSerializer

    '''
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.customer.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    '''




class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    permission_classes = [IsSeller]

    def get_serializer_class(self):
        if self.request.method=="POST":
            return CreateSellerSerializer

        return SellerSerializer

    '''
    def get_permissions(self):
        permission_classes = []
        if self.request.method == "POST":
            permission_classes = [IsSeller]
        return [permission() for permissions in permission_classes]
    '''

    '''
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (seller, created) = Seller.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = SellerSerializer(seller)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = SellerSerializer(seller, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
    '''

