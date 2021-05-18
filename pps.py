#!/usr/bin/pythony
import os, sys
sys.path.append('_import/')
import pjt, directory, cor, port
usr = sys.argv[1] 


pselect = False
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
normal = '\033[0;0m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'



start = azul+""" 
   _________________________________________________________________________
  |	____    __    ____  __       _______.___________. __       _______  |
  |	\   \  /  \  /   / |  |     /       |           ||  |     |   ____| |
  |	 \   \/    \/   /  |  |    |   (----`---|  |----`|  |     |  |__    |
  |	  \            /   |  |     \   \       |  |     |  |     |   __|   |
  |	   \    /\    /    |  | .----)   |      |  |     |  `----.|  |____  |
  |	    \__/  \__/     |__| |_______/       |__|     |_______||_______| |
  |			                                                    |
  |                              a hAcKeR ToOl                              |
  |                           cOdEd By: BuNnYdArK                           |
  |                              vErSiOn: 0.1                               |
  |                           hAcKiNg tHe PlAnEt                            |
  |_________________________________________________________________________|
"""+normal


def getCmd(cmd):
	global target
	global pselect
	global project
	global ip
	cmd = cmd.split(" ")
	if(cmd[0] == "help"):
		if(pselect == False):
			print verde+"""             .: HELP OF COMMANDS :.


	- ajuda = Listar os comandos
	- sair = Sair do programa
	- limpar = limpar terminal
	- add = Adicionar um novo projeto
	- select = selecionar algum projeto ja criado
	- list = listar projetos criados
			"""+normal
			menu()
		elif(pselect == True):
			print verde+"""             .: HELP OF COMMANDS :.


	- ajuda = Listar os comandos
	- sair = Sair do projeto
	- limpar = limpar terminal
	- port = listar ou scanear portas abertas
	- directory = ver alguns diretorios e arquivos
	- information = ver informacoes basicas
			"""+normal
			menu()
	elif(cmd[0] == "sair"):
		if(pselect == True):
			pselect = False
			project = ""
			print "Projeto finalizado com Sucesso!"
			menu()
		else:		
			print "Bye! :)"
			os._exit(0)
	elif(cmd[0] == "limpar"):
		os.system("clear")
		if(pselect == True):
			menuProject(project)
		else:
			menu()
		
	elif(cmd[0] == "add"):
		if(pselect == True):
			print "[!] Saia do projeto atual para criar um novo projeto!"			
			menuProject(project)
		else:	
			try:
				if(cmd[1] != "" and cmd[2] != ""):
					if(cmd[2][:4] != "http"):
						print "[x] Por favor, Coloque https:// ou http://"
						menu()
					else:
						name = cmd[1]
						target = cmd[2]
						pjt.addProject(name, target)
						menu()
				else:
					print "[x] Digite o nome do projeto: add [NOME DO PROJETO] [URL DO PROJETO], exemplo: add google http://www.google.com"
					menu()
			except IndexError:
				print "[x] Digite o nome do projeto: add [NOME DO PROJETO] [URL DO PROJETO], exemplo: add google http://www.google.com"
				menu()
	elif(cmd[0] == "select"):
		if(pselect == False):
			try:		
				if(cmd[1] != ""):
					if(os.path.isdir("projects/"+cmd[1])):
						project = cmd[1]	
						pselect = True
						folder = "projects/"+project+"/target.txt"
						fd = open(folder, "r")
						fd = fd.readlines()
						for x in xrange(0, len(fd)):
							fd[x] = fd[x].split("|")
						for a,b in fd:
							if(a == "Target"):
								site = b.strip("\n")
							elif(a == "IP"):
								ip = b.strip("\n")
						menuProject(project)
					else:
						print "[x] Projeto nao existente, verifique seus projetos com o comando: list"
						menu()
				else:
					print "[x] Digite o nome do projeto, exemplo: select google"
					menu()
			except IndexError:
				print "[x] Digite o nome do projeto, exemplo: select google"
				menu()
		else:
			print "[!] Projeto ja selecionado"
			menuProject(project)
	elif(cmd[0] == "list"):
		if(pselect == True):	
			print "[!] Saia do projeto atual para vizualizar todos os projetos!"
			menuProject(project)
		elif(pselect == False):
			x = os.listdir('projects/')
			print vermelho+"Projetos: \n"
			for p in x:
				print "     [+] "+p
			menu()
	elif(cmd[0] == "information" and pselect == True):
		if(pselect == True):
			p = "projects/"+project+"/target.txt"
			p = open(p)
			p = p.read()
			print azul+p
			menuProject(project)
		else:
			print "[!] Selecione um projeto antes!"
	elif(cmd[0] == "port"):
		if(pselect == True):
			try:
				if(cmd[1] == "scan"):
					port.getPort(ip, project)
					menuProject(project)
				elif(cmd[1] == "list"):
					ports = port.listPort(project)
					for x in ports:
						print x.strip("\n")
					menuProject(project)
				elif(not cmd[1]):
					print "[!] Digite: port scan ou port list "
					menuProject(project)
			except IndexError:
				print "[!] Digite: port scan ou port list "
				menuProject(project)
				
		else:
			print "[!] Selecione o projeto primeiro!"
			menu()
	elif(cmd[0] == "directory"):
		try:
			if(cmd[1] == "find"):
				folder = "projects/"+project+"/directory.txt"
				if(os.path.isfile(folder)):
					print "[!] Diretorios e arquivos ja procurados, digite: directory list"
					menuProject(project)
				else:
					if(pselect == True):
						try:
							if(cmd[1] == "find"):
								directory.run(target, "str/wlDir.txt", project)
								menuProject(project)
						except IndexError:
							print "[!] Digite: port scan ou port list "
							menuProject(project)
					else:
						print "[!] Selecione um projeto antes!"
						menuProject(project)
			elif(cmd[1] == "directory"):
				folder = "projects/"+project+"/directory.txt"
				if(os.path.isfile(folder)):
					dr = open(folder, "r")
					dr = dr.readlines()
					for a in dr:
						print "[+] "+a.rstrip()
					menuProject(project)
				else:
					print "[!]Diretorios e arquivos ainda nao procurados, Digite: direcory find"
					menuProject(project)
		except IndexError:
			print "[!] Digite: directory find ou directory list "
			menuProject(project)
	else:
		if(pselect == True):
			print ciano+cmd[0]+": Command invalid, please write help"+normal
			menuProject(project)
		else:
			print ciano+cmd[0]+": Command invalid, please write help"+normal
			menu()
	

def bar(user, project):
	if(project != ""):
		line = amarelo+user+"@"+project+" $ "+normal
	else:
		line = amarelo+user+" $ "+normal
	c = str(raw_input(line))
	return c

def menu():
	command = bar(usr, "")
	getCmd(command)
def menuProject(pj):
	cmd = raw_input(amarelo+usr+" ["+pj+"] > ")
	getCmd(cmd)
print start
menu()
