import commands
import os

def getPort(ip, project):
		folder = "projects/"+project+"/port.txt"
		print "[+] Pegando informacoes do site..."
		cmd = commands.getoutput('nmap %s' % ip)
		print "[+] Procurando portas abertas..."
		f = open("port__temporary.txt", "w")
		f.write(cmd)
		f.close()
		f = open("port__temporary.txt", "r")
		n = 0
		debug = ""
		for a in f:
			if n > 4:
				debug = debug+a
			n = n+1
		f.close()
		f = open(folder, "w")
		f.write(debug)
		os.remove("port__temporary.txt")
		print "[+] Portas encontradas com sucesso! digite: port list"

def listPort(project):
	folder = "projects/"+project+"/port.txt"
	if(os.path.isfile(folder)):
		ports = open(folder, "r")
		ports = ports.readlines()
		return ports
	else:
		return "Portas ainda nao escaneadas, por favor digite port scan"
