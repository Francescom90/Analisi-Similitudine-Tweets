import sys
import os.path

import twitter_mining
import tf_idf_File_Printer as tfidf
import datetime
import analisi_similitudine as similitudine

operation=words=date=""
have_date=True
argument=len(sys.argv)
file1=file2=''

def validate_date(date_text):
	try:
		datetime.datetime.strptime(date_text, '%d-%m-%Y')
	except ValueError:
		raise ValueError("Formato della data scorretto, deve essere GG-MM-AAAA")
	return True
def check_op(op):
	return op=='analisi'or op=='acquisizione'or op=='completo'


print "Argomenti trovati: %s" %argument

if(argument==1):
	print "non sono stati inseriti parametri adeguati"
	sys.exit()

if(check_op(sys.argv[1])):
	operation=sys.argv[1]
else:
	print "Operazione non valida, operazioni valide: acquisizione e analisi"
	sys.exit()
	
if(operation=="acquisizione"):
	print "operazione: Acquisizione"
	if(argument==4):
		words=sys.argv[2]
		if(validate_date(sys.argv[3])):
			date=sys.argv[3]
	if(argument==3):
		if(validate_date(sys.argv[2])):
			date=sys.argv[2]
		else:
			words=sys.argv[2]
	
	if (words==""):
		if(os.path.isfile("words.txt")):
			with open("words.txt",'r') as input:
				words=input.readline()
	if (date==''):
		have_date=False

	print "ricerca inerente a :%s" %(words,)
	print "la data in esame: %s" %(date,)
	
	twitter_mining.miner(words,date,type)
if(operation=="analisi"):
	if(argument==4):
		if(os.path.isfile(sys.argv[2])and os.path.isfile(sys.argv[3])):
			file1=sys.argv[2]
			file2=sys.argv[3]
	else:
		if(os.path.isfile("to_compare.txt")):
			with open("to_compare.txt",'r') as input:
				file1=input.readline()
				file2=input.readline()
				file1=file1.replace("\n","")
				file2=file2.replace("\n","")
		else:
			sys.exit()
	tfidf.tfidf_run(file1)
	tfidf.tfidf_run(file2)
	path="rated token/"
	
	file1="%s%s" %(path,file1)
	file2="%s%s" %(path,file2)
	
	similitudine.analisi(file1,file2)