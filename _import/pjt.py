import os, socket, admin
def addProject(name, target):
	i = target.replace("https://", "")
	i = target.replace("http://", "")
	folder = "projects/"+name+"/"
	if not os.path.exists(folder):
    		os.makedirs(folder)
		print "[+] Obtendo informacoes basicas do site..."
		pAdmin = admin.find(target, "php") 
		ip = socket.gethostbyname(i)
		print "[+] Criando o projeto..."
		arq = open(folder+name+".txt", "w")
		arq.write("** prijeto inicado em 19:22 **")
		print "[+] Criando logs e arquivos..."
		arq.close()
		arq = open(folder+"target.txt", "w")
		txt = "Target:"+target+"\nIP:"+str(ip)+"\nPagina Admin:"+pAdmin
		arq.write(txt)
		arq.close()
		print "[+] Projeto criado com sucesso!"
	else:
		print "Projeto ja criado!"
	
