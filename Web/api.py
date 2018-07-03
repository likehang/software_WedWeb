import os
from Web.models import *
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django import forms
class singleC_S(serializers.ModelSerializer):
    class Meta:
        model = C_S
        fields='__all__'

@api_view(['GET'])
def getCServer(request):
    print('getCServer')
    if request.method == 'GET':
        token = get_token(request)
        print(token)
        user = request.user
        com = Company.objects.get(manager__belong_to = user)
        ser = C_S.objects.filter(belong = com)
        serializer = singleC_S(ser , many = True)
        return Response(serializer.data)
    else:
        return Response(status=None)
    
@api_view(['GET']) 
def putCServer(request,id):
    print('putCServer')
    if request.method == 'PUT':
        pass
    else:
        return Response(status=None)

class graph(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields = '__all__'

@api_view(['GET','PUT'])
def getserver_graphs(request,id):
    pass

@api_view(['POST','DELETE'])
def putserver_graphs(request):
    pass

class Skinds(serializers.ModelSerializer):
    class Meta:
        model = server_choices
        fields = '__all__'

@api_view(['GET'])
def getServer_kind(request):
    print('getServer_kind')
    kins = server_choices.objects.all()
    serializer = Skinds(kins , many = True)
    return Response(serializer.data)

class singleCom(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name','icon','phone','ident','isopen','inward_phone','business_kind','adress']

class ComForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    icon = forms.ImageField(required = True)
    phone = forms.CharField(max_length=20, required=True)
    isopen = forms.BooleanField(required=True)
    inward_phone = forms.CharField(max_length=20, required=True)
    business_choices = forms.IntegerField(required=True)
    adress = forms.IntegerField(required=True)

@api_view(['GET','POST'])
def manageCompany(request):
    print('manageCompany')
    if request.method == 'GET':
        get_token(request)
        print('get')
        user = request.user
        com = Company.objects.get(manager__belong_to = user)
        serializer = singleCom(com , many = False)
        return Response(serializer.data)

    elif request.method == 'POST':
        print('post')
        user = request.user
        com = Company.objects.get(manager__belong_to = user)
        old_serializer = singleCom(com , many = False)
        reform = request.POST
        print(reform)
        com.name = reform['name']
        if request.FILES:
            com.icon = request.FILES
        else:
            print('no files')
        com.phone = reform['phone']
        com.isopen = bool(reform['isopen'])
        com.inward_phone = reform['inward_phone']
        com.business_kind.id = reform['business_kind']
        com.adress.id = reform['adress']
        com.save()
        serializer = singleCom(com , many = False)
        return Response(serializer.data)
        
        # if new_serializer.is_valid():
        #     if os.path.exists(MEDIA_ROOT+com.icon):
        #         print('exist')
        #         return Response(new_serializer.data,status=None)
        #     else:
        #         print('false')
        #         return Response(old_serializer.data,status=None)
        # else:
        #     print(new_serializer.errors)
        #     return Response(old_serializer.data,status=None)
    else:
        return Response(old_serializer.data,status=None)


class Orderlist(serializers.ModelSerializer):
    class Meta:
        model = Order_list
        fields = '__all__'
        depth = 2

@api_view(['GET'])
def getClist(request):
    if request.method == 'GET':
        user = request.user
        com = Company.objects.get(manager__belong_to = user)
        lists = Order_list.objects.filter(needlist__belong = com)
        serializer = Orderlist(lists,many = True)
        return Response(serializer.data)
    else:
        return Response(status=None)

@api_view(['POST'])
def manageOrderList(request,id):
    if request.method == 'POST':
        The_list = Order_list.objects.get(id=id)
        msg = request.POST['next']
        if msg =='cancel':
            The_list.status.status_level = The_list.status.next_2
        else:
            The_list.status.status_level = The_list.status.next_1
        The_list.save()

        user = request.user
        com = Company.objects.get(manager__belong_to = user)
        lists = Order_list.objects.filter(needlist__belong = com)
        serializer = Orderlist(lists,many = True)
        return Response(serializer.data)
    else:
        return Response(status=None)

@api_view(['PUT'])
def newlist(request):
    pass

class FavList(serializers.ModelSerializer):
    class Meta:
        model = Fav
        fields = '__all__'

@api_view(['GET','POST','DELETE'])
def manageFav(request,id):
    if request.mathod == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return Response(status=None)
    

class Business_kind(serializers.ModelSerializer):
    class Meta:
        model = business_choices
        fields = '__all__'
@api_view(['GET'])
def getBusinessKind(request):
    kind = business_choices.objects.all()
    serializer = Business_kind(kind ,many = True)
    print('getBusinessKind')
    return Response(serializer.data)

class serCity(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
@api_view(['GET'])
def getCity(request):
    kind = City.objects.all()
    serializer = serCity(kind ,many = True)
    print('getCity')
    return Response(serializer.data)