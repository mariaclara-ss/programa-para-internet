from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=90)
    telefone = models.CharField(max_length=15)
    endereco_entrega = models.CharField(max_length=160)
    data_cadastro = models.DateField()

class Funcionarios(models.Model):
    nome = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    cargo = models.CharField(max_length=80)
    data_admissao = models.DateField()
    salario = models.IntegerField()

class Fornecedores(models.Model):
    cnpj = models.CharField(max_length=15)
    nome_fornecedor = models.CharField(max_length=70)
    razao_social = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=150)

class Pecas(models.Model):
    codigo = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=16)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

# Create your models here.
