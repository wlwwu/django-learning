from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from api import models
from api import serializers
from api import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """return a list of apiview features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                   serializer.errors,
                   status=status.HTTP_400_BAD_REQUEST
                            )
    
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self,reuqest,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """DELETE an object"""
        return Response({'method':'DELETE'})


#create viewset
class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    #share some serilizer with apiview
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset = [
            'User actions (list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'Hello!','a_viewset': a_viewset})
    
    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
           name = serializer.validated_data.get('name')
           message = f'Hello {name}!'
           return Response({'message':message})
        else:
            return Response(
                   serializer.errors,
                   status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self,request,pk=None):
        """handle getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """handle updating an object via its id"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """handle updating part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """handle removing an object"""
        return Response({"http_method":'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    ##add permission and auth to viewset
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    ##add search profile feature
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


