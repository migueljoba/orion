# -*-encoding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# $ python manage.py migrate

# $ python manage.py makemigrations contribuyentes

# $ python manage.py sqlmigrate contribuyentes 0001

# $ python manage.py migrate

# para relacionar varios objetos de una vez
# https://docs.djangoproject.com/en/1.10/intro/tutorial07/

@python_2_unicode_compatible
class ContribuyenteTipo(models.Model):
    TIPO = (
        ('F', 'Físico'),
        ('J', 'Jurídico'),
    )

    tipo = models.CharField('Tipo de contribuyente', max_length=1, choices=TIPO)
    descripcion = models.CharField('Descripcion', max_length=50)

    def __str__(self):
        return '%s - %s' % (self.tipo, self.descripcion)


@python_2_unicode_compatible
class Contribuyente(models.Model):
    ruc = models.CharField(primary_key=True, max_length=11)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    tipo = models.ForeignKey(to=ContribuyenteTipo, null=True)
    registrado_desde = models.DateField('Registrado desde')

    # Django convention is to use the empty string, not NULL
    registrado_hasta = models.DateField('Registrado hasta', blank=True, null=True)

    def __str__(self):
        return '%s %s, %s' % (self.ruc, self.apellido, self.nombre)

    def save(self, *args, **kwargs):
        super(Contribuyente, self).save(*args, **kwargs)
