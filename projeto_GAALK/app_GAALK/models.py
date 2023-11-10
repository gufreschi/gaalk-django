from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    data_nascimento = models.DateField()
    telefone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=30)
    conf_senha = models.CharField(max_length=30)