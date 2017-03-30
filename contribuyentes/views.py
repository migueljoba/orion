# -*-encoding:utf-8-*-

import os

from django.contrib.auth.models import User
from django.http import HttpResponse
from models import Contribuyente, ContribuyenteTipo
from rest_framework import generics
from rest_framework import permissions
from serializers import ContribuyenteSerializer, UserSerializer


class ContribuyenteLista(generics.ListCreateAPIView):
    queryset = Contribuyente.objects.all()
    serializer_class = ContribuyenteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ContribuyenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contribuyente.objects.all()
    serializer_class = ContribuyenteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    tipo = ContribuyenteTipo.objects.filter(id=1)[0]

    # path del directorio del script que se ejecuta
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    filenames = ['ruc0.txt',
                 'ruc1.txt',
                 'ruc2.txt',
                 'ruc3.txt',
                 'ruc4.txt',
                 'ruc5.txt',
                 'ruc6.txt',
                 'ruc7.txt',
                 'ruc8.txt',
                 'ruc9.txt'
                 ]

    for fn in filenames:
        # prepara el path para el archivo actual.
        file_path = os.path.join(BASE_DIR, 'datasource', fn)
        print 'Leyendo %s' % fn

        with open(file_path) as f:

            # contador para el número de línea del archivo
            i = 0

            while True:
                print i
                line = f.readline()

                if not line:
                    # se llegó al fin del archivo. No hay líneas por consumir
                    break

                i += 1

                # separar cada linea mediante el '|'
                data = line.strip().split('|')

                contri = contributor(data)

                c = Contribuyente(ruc=contri['ruc'],
                                  nombre=contri['nombre'],
                                  apellido=contri['apellido'],
                                  tipo=tipo,
                                  registrado_desde='2017-03-29')

                c.save()

    return HttpResponse("FIN")


def contributor(data):
    ruc = '%s-%s' % (data[0], data[2])
    full_name = data[1].split(',') + ['']
    first_name = full_name[1].strip()
    last_name = full_name[0].strip()

    return {'ruc': ruc, 'nombre': first_name, 'apellido': last_name}
