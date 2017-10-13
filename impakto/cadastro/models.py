# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Cadastro(models.Model):
	
	

	SITUACAO_CHOICES = (
		(u'autor', u'Autor'),
		(u'reu', u'Reu'),
		(u'advogado_Autor', u'Advogado do Autor'),
		(u'advogado_Reu', u'Advogado do Reu'),
		)

	ESTADO_CHOICES = (
		(u'AC', u'Acre'),
		(u'AL', u'Alagoas'),
		(u'AP', u'Amapa'),
		(u'AM', u'Amazonas'),
		(u'BA', u'Bahia'),
		(u'CE', u'Ceará'),
		(u'DF', u'Distrito Federal'),
		(u'ES', u'Espirito Santo'),
		(u'GO', u'Goias'),
		(u'MA', u'Maranhão'),
		(u'MT', u'Mato Grosso'),
		(u'MS', u'Mato Grosso do Sul'),
		(u'MG', u'Minas Gerais'),
		(u'PA', u'Para'),
		(u'PB', u'Paraiba'),
		(u'PR', u'Parana'),
		(u'PE', u'Pernambuco'),
		(u'RJ', u'Rio de Janeiro'),
		(u'RN', u'Rio Grande do Norte'),
		(u'RS', u'Rio Grande do Sul'),
		(u'RR', u'Roraima'),
		(u'RO', u'Rondonia'),
		(u'SC', u'Santa Catarina'),
		(u'SP', u'Sao Paulo'),
		(u'SE', u'Sergipe'),
		(u'TO', u'Tocantins'),
		)

 	cadastro_codigo = models.AutoField(primary_key=True)
	cadastro_nome = models.CharField(max_length = 100)
	cadastro_email = models.CharField(max_length = 30)
	cadastro_situacao = models.CharField(choices = SITUACAO_CHOICES, max_length = 20)

# endereço
	cadastro_logradouro = models.CharField(max_length = 100)
	cadastro_numero = models.CharField(max_length = 6)
	cadastro_complemento = models.CharField(max_length = 20)
	cadastro_cep = models.CharField(max_length = 15)
	cadastro_bairro = models.CharField(max_length = 30)
	cadastro_cidade = models.CharField(max_length = 30)
	cadastro_estado = models.CharField(choices = ESTADO_CHOICES, max_length = 20)

	cadastro_observacao = models.TextField()


class Pessoa(Cadastro):
	cadastro_cpf = models.CharField(max_length = 16)

class Empresa(Cadastro):
	cadastro_cnpj = models.CharField(max_length = 25)