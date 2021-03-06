"""orion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from contribuyentes.views import ContribuyenteLista, ContribuyenteDetail, UserList, UserDetail

# Serializers define the API representation.
"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
"""

# ViewSets define the view behavior.
"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserList)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/contribuyentes/$', ContribuyenteLista.as_view()),
    url(r'^api/contribuyentes/(?P<pk>[\w\-]+)/$', ContribuyenteDetail.as_view()),

    url(r'^api/users/$', UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),

    # vistas externas
    url(r'^contribuyentes/', include('contribuyentes.urls')),

]

from rest_framework.authtoken import views

urlpatterns += [
    url(r'^get_token/', views.obtain_auth_token)
]
