
from django.db import models
from datetime import datetime


class Room(models.Model):
    """Room : Room unico que agrupa mensajes para el CHAT"""
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)


class Message(models.Model):
    """Message : Message por Usuario agrupados por Room"""
    value = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)