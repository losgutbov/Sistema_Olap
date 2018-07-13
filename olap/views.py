from django.shortcuts import render
from .codigo_olap import Operacao

# Create your views here.

def index(request):
	op = Operacao()
	tabela, cab = op.condicaoInicial()
	tabela2, cab2 = op.condicaoExpansaoLinhas()

	dados = {'tabela': tabela2, 'cab': cab2}
	return render(request, 'olap/index.html', {'dados': dados})