# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MoedaVirtual(models.Model):
	nome_moeda = models.CharField(max_length=30)
	cotacao = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.nome_moeda + ' - ' + str(self.cotacao)