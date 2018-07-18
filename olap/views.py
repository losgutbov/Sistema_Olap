from django.shortcuts import render
from .codigo_olap import Operacao

# Create your views here.

def index(request):
	op = Operacao()
	tabela, cab = op.condicaoInicial()
	tabela2, cab2 = op.condicaoExpansaoLinhas()

	if request.method == 'POST':
		novoEstado, lin = op.transformacaoEstado(request.POST['estado'], request.POST['mudanca'])
		lin2, orientacao, cab3, subcab, cols = op.formacaoMatriz(novoEstado, lin)
	else:
		novoEstado, lin = op.transformacaoEstado('0-0-0-0-0-', 'NADA')
		lin2, orientacao, cab3, subcab, cols = op.formacaoMatriz(novoEstado, lin)
		
	dados = {'tabela': tabela2, 'cab': cab3, 'estado': novoEstado, 'lin': lin2, 'orientacao': orientacao, 'subcab': subcab, 'cols': cols}
	return render(request, 'olap/index.html', {'dados': dados})