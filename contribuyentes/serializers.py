# -*-encoding:utf-8-*-
from django.contrib.auth.models import User
from models import Contribuyente
from rest_framework import serializers


# http://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers

class ContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuyente
        fields = ('ruc', 'nombre', 'apellido', 'registrado_desde')




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')