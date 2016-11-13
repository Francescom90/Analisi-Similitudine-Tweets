# -*- coding: cp1252 -*-
#test vettore
from vector_maker import normalize,crea_vettore_comulato,compare_vector
import sys

def analisi(file1,file2):
	
	path="rated token/"
	export="result.txt"
	print export
	sys.stdout=open(export,"w")
	
	print "Confronto %s-%s:"%(file1,file2)
	risultato=compare_vector(file1,file2)
	#print "%02d - %s"%(n,risultato)
	print risultato