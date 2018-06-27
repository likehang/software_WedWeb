import os
from Web.models import *
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token

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
        new_serializer = singleCom(data = request.data)
        print(new_serializer)
        if new_serializer.is_valid():
            if os.path.exists(MEDIA_ROOT+com.icon):
                print('exist')
                return Response(new_serializer.data,status=None)
            else:
                print('false')
                return Response(old_serializer.data,status=None)
        else:
            print(new_serializer.errors)
            return Response(old_serializer.data,status=None)
    else:
        return Response(old_serializer.data,status=None)


class Orderlist(serializers.ModelSerializer):
    class Meta:
        model = Order_list
        fields = '__all__'

@api_view(['GET','PUT'])
def manageOrderList(request,id):
    if request.mathod == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    else:
        return Response(status=None)

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