# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Cliente(models.Model):
	
	SITUACAO_CHOICES = (
		(u'Autor', u'Autor'),
		(u'Reu', u'Reu'),
		(u'Advogado do Autor', u'Advogado do Autor'),
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

	DESCONTO_CHOICES = (
		(u'5', u'5%'),
		(u'10', u'10%'),
		(u'15', u'15%'),
		(u'20', u'20%'),
		(u'25', u'25%'),
		(u'30', u'30%'),
		(u'35', u'35%'),
		(u'40', u'30%'),
		(u'45', u'45%'),
		(u'50', u'40%'),
		(u'55', u'55%'),
		(u'60', u'60%'),
		(u'65', u'65%'),
		(u'70', u'60%'),
		(u'75', u'75%'),
		(u'80', u'80%'),
		(u'85', u'85%'),
		(u'90', u'90%'),
		(u'95', u'95%'),
		(u'100', u'100%'),
		)

 	codigo = models.AutoField(primary_key=True, unique = True)
	nome = models.CharField(max_length = 100, verbose_name = "Nome do Cliente")
	email = models.CharField(max_length = 30, verbose_name = "Email")
	situacao = models.CharField(choices = SITUACAO_CHOICES, max_length = 20, 
		verbose_name = "Situação do Cliente")
	cpf_cpnj= models.CharField(max_length = 30, unique = True, 
		verbose_name = "CPF ou CNPJ") # se tiver 14, é CPF, se tiver 25 é CNPJ
	
	# endereço
	logradouro = models.CharField(max_length = 100, verbose_name = "Logradouro")
	numero = models.CharField(max_length = 6, verbose_name = "Numero")
	complemento = models.CharField(max_length = 20, verbose_name = "Complemento")
	cep = models.CharField(max_length = 15, verbose_name = "CEP")
	bairro = models.CharField(max_length = 30, verbose_name = "Bairro")
	cidade = models.CharField(max_length = 30, verbose_name = "Cidade")
	estado = models.CharField(choices = ESTADO_CHOICES, max_length = 20, verbose_name = "Estado")

	valor_desconto= models.CharField(choices = DESCONTO_CHOICES, max_length = 5, verbose_name = "Receberá de desconto")
	observacao_texto = models.TextField(verbose_name = "Observações sobre sobre o cliente")

class Processo(models.Model):

	SITUACAO_CHOICES = (
		(u'1 instancia', u'1 instancia'),
		(u'2 instancia', u'2 instancia'),
		(u'3 instancia', u'3 instancia'),
		(u'Execução', u'Execução'),
	)
	
	codigo_cliente = models.ForeignKey(Cliente)
	numero_processo = models.CharField(max_length = 25 , unique = True) 
	
	situacao_processo = models.CharField(choices = SITUACAO_CHOICES, max_length = 20, 
		verbose_name = "Situação do Processo")
	cidade = models.CharField(max_length = 30, verbose_name = "Cidade")
	vara =  models.CharField(max_length = 3	, verbose_name = "Vara")
	# nome_cliente = models.CharField(max_length = 100, nome.Cadastro, )
	# colocar o nome do cliente para faturamento depois
	nome_autor = models.CharField(max_length = 100, verbose_name = "Nome do Autor")
	nome_reu = models.CharField(max_length = 100, verbose_name = "Nome do Reu")
	nome_adv_autor = models.CharField(max_length = 100, verbose_name = "Nome do Advogado do Autor")
	nome_adv_reu  = models.CharField(max_length = 100, verbose_name = "Nome do Advogado do Reu")
	data_entrada = models.DateField(verbose_name = "Data de Entrada")
	prazo_final = models.DateField(verbose_name = "Prazo Final")
 	data_saida = models.DateField(verbose_name = "Data de Saida")
 	
class Servico(models.Model):

	TIPOSALARIO_CHOICES = (
		(u'Hora', u'Hora'),
		(u'Ḿes', u'Mes'),
	)

	TIPODEMISSAO_CHOICES = (
		(u'Sem Justa causa', u'Sem Justa causa'),
		(u'Justa', u'Justa'),
	)

	STATUS_CHOICES = (
		(u'Em Espera', u'Em Espera'),
		(u'Em trabalho', u'Em trabalho'),
		(u'Em faturamento', u'Em faturamento'),
		(u'Faturado', u'Faturado'),	
	)

	
	codigo_processo = models.ForeignKey(Processo)
	data_admissao = models.DateField(verbose_name = "Data de Admissão")
	data_demissao = models.DateField(verbose_name = "Data de Demissão")
	data_distribuido = models.DateField(verbose_name = "Data em que o processo saiu da vara trabalhista (distribuido)")

	tipo_salario = MultiSelectField(choices = TIPOSALARIO_CHOICES, max_choices = 1, 
 		verbose_name = "Tipo Salario")

	tipo_demissao = MultiSelectField(choices = TIPODEMISSAO_CHOICES, max_choices = 1, 
 		verbose_name = "Tipo Demissao")

	status_processo = models.CharField(choices = STATUS_CHOICES, max_length = 20, 
		verbose_name = "Status do Processo")
	

	principal_atualizado =  models.CharField(max_length = 30, verbose_name = "Principal Atualizado")
	juros_mora =  models.CharField(max_length = 30, verbose_name = " Juros de Mora")
	total_bruto =  models.CharField(max_length = 30, verbose_name = "Total Bruto")
	inss_autor = models.CharField(max_length = 30, verbose_name = "INSS Autor")
	irrf =  models.CharField(max_length = 30, verbose_name = "I.R.R.F")

	informacoes_calculo = models.TextField(verbose_name = "Dados e informações para calculo")


class Calculo(models.Model):

	TRABALHOSEXECUTADO_CHOICES = (
		(u'Imp. Calculo', u'Imp. Calculo'),
		(u'Imp. Laudo', u'Imp. Laudo'),
		(u'Atual. Valores', u'Atual. Valores'),
		(u'Laudo para Inicial', u'Laudo para Inicial'),
		(u'Apresentação de calculos', u'Apresentação de calculos'),
		(u'Impugnação /. Embargos', u'Impugnação /. Embargos'),
		(u'Calculo Contigencia', u'Calculo Contigencia'),
		(u'Perito do Juizo', u'Perito do Juizo'),
		(u'Quesitos', u'Quesitos'),
	)

	JUSTICA_CHOICES = (
		(u'Civel', u'Civel'),
		(u'Trabalhista', u'Trabalhista'),
		(u'Civel Fed.', u'Civel Fed.'),
	)
	PAGAMENTO_CHOICES = (
		(u'A vista / Na entrega', u'A vista / Na entrega'),
		(u'Faturado', u'Faturado'),
	)

	codigo_servico = models.ForeignKey(Servico)
	
	trabalhos_executados =  MultiSelectField(choices = TRABALHOSEXECUTADO_CHOICES, max_choices = 9, 
 		verbose_name = "Tipo Salario")

	justica =  MultiSelectField(choices = JUSTICA_CHOICES, max_choices = 1, 
 		verbose_name = "Justiça")

	tipo_pagamento =  MultiSelectField(choices = PAGAMENTO_CHOICES, max_choices = 1, 
 		verbose_name = "Tipo Salario")

	valor =  models.FloatField(verbose_name = "Valor")

	vencimento = models.DateField(verbose_name = "Data de vencimento")



class Fatura(models.Model):
	SERVICO_CHOICES = (
		(u'Calculos Trabalhistas', u'Calculos Trabalhistas'),
		(u'Assistencia Tecnica em Pericia', u'Assistencia Tecnica em Pericia'),
		(u'Engenharia de Segurança de Trabalho', u'Engenharia de Segurança de Trabalho'),
		(u'Auditoria Trabalhista', u'Auditoria Trabalhista'),
	)

	SERVICO_CHOICES = (
		(u'Por Mes e por demanda', u'Por Mes e por demanda'),
		(u'Por Mes e por preço fixo', u'Por Mes e por preço fixo'),
		(u'Por demanda', u'Por demanda'),
	)


	codigo_calculo = models.ForeignKey(Calculo)

	servicos_escolhas = MultiSelectField(choices = SERVICO_CHOICES, max_choices = 4, 
 		verbose_name = "Serviços a serem escolhidos")
	
	tipo_fatura = MultiSelectField(choices = SERVICO_CHOICES, max_choices = 4, 
 		verbose_name = "Tipo de fatura")

	numero_processo = models.CharField(max_length = 100, verbose_name = "Numero do processo")
	nome_autor  =  models.CharField(max_length = 100, verbose_name = "Nome do autor")

	numero_autores = models.IntegerField(verbose_name = "Numero de autores")

	valor = models.FloatField(verbose_name = "Valor a cobrar")
	data_entrega = models.DateField(verbose_name = "Data de vencimento")
