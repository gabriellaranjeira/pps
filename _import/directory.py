import sys, urllib2, time, os
def run(site, wl, pjt):
	user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv19.0) Gecko/20100101 Firefox/19.0"
	path = []
	if(site[len(site)-1] != "/"):
		site = site+"/"

	def buildWordlist(wl_file):
		fd = open(wl_file, "r")
		word = fd.readlines()
		for words in word:
			words = words.rstrip()
			l = len(words)
			if (words[l-1] != "/"):
				words = words+".php"
			path.append(words)

	def validHost(host):	
		try:	
			host = host+"jgk45vk6j4g5vk7jg3v64k7jg3kj65g7vkjf356gf7jk3g6fkj7g.php"
			headers = {}
			headers["User-Agent"] = user_agent
			r = urllib2.Request(host,headers=headers)
			url = urllib2.urlopen(r)
			if(url.code == 200):
				status = "ERROR"
		except:
			status = "OK"
		return status
	

	def teste(path, host):
		if(validHost(host) == "OK"):
			try:
				host = site+path
				headers = {}
				headers["User-Agent"] = user_agent
				r = urllib2.Request(host,headers=headers)
				url = urllib2.urlopen(r)
				slot = open("log.txt", "a")
				slot.write(path+"\n")
				del(url)
				del(r)
			except :
				pass
		else:
			print "Nao foi possivel identificar as paginas do site !"
			os._exit(0)

	

	def main():
	    for i in range(len(path)):
		try:		
			porc = float((i*100.0) / len(path))
		except ZeroDivisionError:
			porc = 0
		porc = "%.1f" % porc
		porc = str(porc)+"%"
		sys.stdout.write("Procurando paginas e diretorios: [%s]\r" % (porc))
		sys.stdout.flush()
		teste(path[i], site) 

	def validaPath(project):
		f = open("log.txt", "r")
		f = f.readlines()
		d = ""
		a = ""
		for x in f:
			x = x.rstrip()
			if(x[len(x)-1] == "/"):
				d = d+x+"\n"
			else:
				a = a+x+"\n"
		del(f)
		f = open("projects/"+project+"/directory.txt", "w")
	
		f.write(d+a)
		f.close()
		os.remove("log.txt")
	 
	buildWordlist(wl)
	main()
	validaPath(pjt)
	print "Procurando paginas e diretorios: [100%]\n Paginas e Diretorios encontrados com sucesso!\n Use o comando: files :)"
