# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from impakto.cadastro.models import Cadastro
from impakto.cadastro.models import Processo

class CadastroAdmin(admin.ModelAdmin):
	model = Cadastro
	list_display = ['codigo', 'nome', 'situacao']
	list_filter = ['cpf_cpnj', 'situacao']
	search_fields = ['situacao']
	save_on_top = True
admin.site.register(Cadastro, CadastroAdmin)

class ProcessoAdmin(admin.ModelAdmin):
	model = Processo
	list_display = ['codigo_cliente', 'numero_processo', 'status_processo', 'situacao_processo']
	list_filter = ['data_entrada', 'prazo_final', 'data_saida']
	search_fields = ['status_processo']
	save_on_top = True
admin.site.register(Processo, ProcessoAdmin)