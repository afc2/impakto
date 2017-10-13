# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from impakto.cadastro.models import Cadastro

class CadastroAdmin(admin.ModelAdmin):
	model = Cadastro
	list_display = ['cadastro_codigo', 'cadastro_nome', 'cadastro_email']
	list_filter = ['cadastro_cidade', 'cadastro_bairro']
	search_fields = ['cadastro_nome']
	save_on_top = True
admin.site.register(Cadastro, CadastroAdmin)