# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *

import requests
import json

# Create your views here.

def index(request):
	ok = True
	teste = ''
	valores = ''

	try:
	    teste = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
	    valores = json.loads(teste.text)
	except Exception, e:
		ok = False
		print e.message    	

	if ok:
	    mv = MoedaVirtual.objects.all()
	    mv.delete()

	    for moeda in valores['valores']:
	    	# for moeda in valores['valores'][valor]:
			mv = MoedaVirtual()
			mv.nome_moeda = valores['valores'][moeda]['nome']
			mv.cotacao = valores['valores'][moeda]['valor']
			mv.save()

	mv = MoedaVirtual.objects.all()
	context = { 'moedas_virtuais': mv }
	return render(request, 'index.html', context)

def consulta(request):
	
	moeda = request.GET.get('moeda','USD')
	investimento = request.GET.get('investimento', 0)
	data = ''

	if investimento > 0:
		valor_moeda = MoedaVirtual.objects.get(nome_moeda=moeda).cotacao
		moeda_investida = int(investimento)/valor_moeda
	else:
		moeda_investida = -1
	return HttpResponse(moeda_investida)		