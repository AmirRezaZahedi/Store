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


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsCustomer]

    '''
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
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
    serializer_class = SellerSerializer
    permission_classes = [IsSeller]

    '''
    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response('ok')
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


