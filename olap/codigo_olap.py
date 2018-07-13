import pandas as pd 
import math
#import numpy

class Operacao(object):
	"""docstring for Operacao"""
	def __init__(self):
		self.data = pd.read_excel('ocupacao.xlsx')

	def porAno(self, ano):
	    lista = list()
	    for col in self.data.columns:
	        if(col.find(ano)>-1):
	            lista.append(col)
	    return lista

	def somarColunas(self, colunas):
	    lista = list()
	    for col in colunas:
	        valor = self.data[col].sum()
	        if math.isnan(valor):
	        	lista.append(0)
	        else:
	        	lista.append(valor)

	    return lista

	def somarLinhas(self, colunas):
	    lista = list()
	    for linha in range(self.data.shape[0]):
	        soma = 0
	        for col in colunas:
	            valor = self.data.loc[linha][col]
	            if not math.isnan(valor):
	                soma = soma + valor 
	        lista.append(soma)
	    
	    return lista


	def condicaoInicial(self):
		ano_2014 = self.porAno('2014')
		col_2014 = self.somarColunas(ano_2014)
		ano_2015 = self.porAno('2015')
		col_2015 = self.somarColunas(ano_2015)
		ano_2016 = self.porAno('2016')
		col_2016 = self.somarColunas(ano_2016)
		ano_2017 = self.porAno('2017')
		col_2017 = self.somarColunas(ano_2017)
		cab = ['Periodo (hr)', '2014', '2015', '2016', '2017']
		lista = list()
		lista.append('DIA')
		lista.append(sum(col_2014))
		lista.append(sum(col_2015))
		lista.append(sum(col_2016))
		lista.append(sum(col_2017))

		listaGlobal = list()
		listaGlobal.append(lista)

		return listaGlobal, cab


	def condicaoExpansaoLinhas(self):
		ano_2014 = self.porAno('2014')
		lin_2014 = self.somarLinhas(ano_2014)
		ano_2015 = self.porAno('2015')
		lin_2015 = self.somarLinhas(ano_2015)
		ano_2016 = self.porAno('2016')
		lin_2016 = self.somarLinhas(ano_2016)
		ano_2017 = self.porAno('2017')
		lin_2017 = self.somarLinhas(ano_2017)
		cab = ['Periodo (hr)', '2014', '2015', '2016', '2017']
		lista = list()
		for linha in range(1,13):
			listaLin = list()
			listaLin.append(linha)
			listaLin.append(lin_2014[linha-1])
			listaLin.append(lin_2015[linha-1])
			listaLin.append(lin_2016[linha-1])
			listaLin.append(lin_2017[linha-1])
			lista.append(listaLin)

		return lista, cab


	