def valid(cor):
	if(cor != "vermelho" or cor != "verde" or cor != "azul" or cor != "ciano" or cor != "magneta" or cor != "padrao" or cor != "amarelo"):
		print "[!] Cor invalida, por favor coloque uma cor valida\nCores validas: vermelho, verde, azul, ciano, magneta, padrao e amarelo !"
	else:
		cor.replace("vermelho", '\033[31m')
		cor.replace("verde", '\033[32m')
		cor.replace("azul", '\033[34m')
		cor.replace("ciano", '\033[36m')
		cor.replace("magneta", '\033[35m')
		cor.replace("padrao", '\033[0;0m')
		cor.replace("amarelo", '\033[33m')
		return cor
