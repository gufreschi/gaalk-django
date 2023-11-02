from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    cpf = models.IntegerField(unique='')
    data_nascimento = models.DateField()
    telefone = models.IntegerField(unique='')
    email = models.EmailField(unique='')
    senha = models.CharField(max_length=30)
    conf_senha = models.CharField(max_length=30)