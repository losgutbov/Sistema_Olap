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


	def completo(self, colunas):
		lista = list()
		i = 0
		for linha in range(self.data.shape[0]):
			listalin = list()
			for col in colunas:
				valor = self.data.loc[linha][col]
				if not math.isnan(valor):
					listalin.append(valor)
				else:
					listalin.append(0)
			lista.append(listalin)
	    
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


	def transformacaoEstado(self, estado, mudanca):
		#periodo, ano1, ano2, ano3, ano4 = estado.split("-")
		vetor = estado.split("-")
		cab = ['Periodo (hr)', '2014', '2015', '2016', '2017']
		i=0
		novoEstado = ''
		for x in cab:
			if x == mudanca:
				if vetor[i]=='0':
					vetor[i]='1'
				else:
					vetor[i]='0'

			novoEstado = novoEstado+vetor[i]+'-'
			i=i+1

		lista = list()
		for i in range(1, 5):
			
			if vetor[0] == '1':
				if vetor[i] == '1':
					ano = self.porAno(cab[i])
					comp = self.completo(ano)
					lista.append(comp)
				else:
					ano = self.porAno(cab[i])
					lin = self.somarLinhas(ano)
					lista.append(lin)

			else:
				if vetor[i] == '1':
					ano = self.porAno(cab[i])
					col = self.somarColunas(ano)
					lista.append(col)
				else:
					ano = self.porAno(cab[i])
					col = self.somarColunas(ano)
					lista.append(sum(col))
			
		return novoEstado, lista

	def formacaoMatriz(self, estado, lista_original):
		vetor = estado.split("-")
		lista = list()
		cab = [['Periodo (hr)', 1], ['2014', 1], ['2015', 1], ['2016', 1], ['2017', 1]]
		meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAIO', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
		subcab = list()
		orientacao = False
		colspan = 0
		subcab.append('-')
		for vet in range(1,5):
			if vetor[vet] == '1':
				for mes in meses:
					subcab.append(mes)
					colspan = colspan + 1
			else:
				subcab.append('-')
				colspan = colspan + 1

		if vetor[0] == '0':
			orientacao = False
			lista.append('DIA')
			posi = 1
			for lis in lista_original:
				totcol = 0
				if vetor[posi] == '1':
					for cel in lis:
						lista.append(cel)
						totcol = totcol+1
					cab[posi][1] = totcol
				else:
					lista.append(lis)
					cab[posi][1] = 1
				posi=posi+1
		else:
			orientacao = True
			for x in range(1,13):
				listalin = list()
				listalin.append(x)
				if vetor[1]== '1':
					for cel in lista_original[0][x-1]:
						listalin.append(cel)
					cab[1][1] = 12
				else:
					listalin.append(lista_original[0][x-1])
					cab[1][1] = 1

				if vetor[2]== '1':
					for cel in lista_original[1][x-1]:
						listalin.append(cel)
					cab[2][1] = 12
				else:
					listalin.append(lista_original[1][x-1])
					cab[2][1] = 1
				
				if vetor[3]== '1':
					for cel in lista_original[2][x-1]:
						listalin.append(cel)
					cab[3][1] = 12
				else:
					listalin.append(lista_original[2][x-1])
					cab[3][1] = 1

				if vetor[4]== '1':
					for cel in lista_original[3][x-1]:
						listalin.append(cel)
					cab[4][1] = 12
				else:
					listalin.append(lista_original[3][x-1])
					cab[4][1] = 1

				lista.append(listalin)
				
		return lista, orientacao, cab, subcab, colspan 
