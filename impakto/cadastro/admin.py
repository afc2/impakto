# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from impakto.cadastro.models import Cliente
from impakto.cadastro.models import Processo
from impakto.cadastro.models import Servico
from impakto.cadastro.models import Calculo
from impakto.cadastro.models import Fatura


class ClienteAdmin(admin.ModelAdmin):
	model = Cliente
	list_display = ['codigo', 'nome', 'situacao']
	list_filter = ['cpf_cpnj', 'situacao']
	search_fields = ['situacao']
	save_on_top = True
admin.site.register(Cliente, ClienteAdmin)

class ProcessoAdmin(admin.ModelAdmin):
	model = Processo
	list_display = ['codigo_cliente', 'numero_processo']
	list_filter = ['data_entrada', 'prazo_final', 'data_saida', 'situacao_processo']
	save_on_top = True
admin.site.register(Processo, ProcessoAdmin)

class ServicoAdmin(admin.ModelAdmin):
	model = Servico
	list_display = ['codigo_processo', 'data_admissao', 'data_demissao', 'data_distribuido']
	search_fields = ['status_escolha']
	save_on_top = True
admin.site.register(Servico, ServicoAdmin)

class CalculoAdmin(admin.ModelAdmin):
	model = Calculo
	list_display = ['codigo_servico', 'valor','vencimento']
	save_on_top = True
admin.site.register(Calculo, CalculoAdmin)

class FaturaAdmin(admin.ModelAdmin):
	model = Fatura
	list_display = ['codigo_calculo', 'numero_processo', 'nome_autor', 'numero_autores', 'valor', 'data_entrega']
	list_filter = ['numero_processo', 'data_entrega']
	search_fields = ['numero_processo']
	save_on_top = True
admin.site.register(Fatura, FaturaAdmin)