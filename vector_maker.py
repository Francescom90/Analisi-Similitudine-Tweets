# -*- coding: cp1252 -*-

import math

#tentativo di creazione per un array di vettori. Ogni vettore rappresenta uno dei tweet della giornata
def crea_array_vettori(file):
	#apro il file contenente i punteggi tf-ifd
	vectors=[]
	with open(file,"r") as input_file:
		vettore={}
		#per ogni linea che corrisponde ad un tweet
		for line in input_file:
			#spezzo il punteggio tf-idf del tweet in una lista dei singoli punteggi delle words
			token=line.split()
			#per ogni singola coppia words-punteggio
			for t in token:
				#divido word e punteggio
				x=t.split(":")
				key=x[0]
				value=x[1]
				#le assegno come chiave-valore di un dizionario
				vettore[key]=value
			vectors.append(vettore)

#tentativo di creazione vettore cumulato
def crea_vettore_comulato(file):
	vettore={}
	with open(file,"r") as input_file:
		for line in input_file:
			token=line.split()
			for t in token:
				x=t.split(":")
				key=x[0]
				value=x[1]
				vettore[key]=float(vettore.get(key,0))+float(value)
	return vettore


def normalize(d, target=1.0):
   raw = sum(d.values())
   factor = target/raw
   return {key:value*factor for key,value in d.iteritems()}

def normalize_vector(d):
	norma=0
	for k in d.keys():
	    norma+=d.get(k)*d.get(k)
	norma=math.sqrt(norma)
	if norma!=0:
		factor=1/norma
	else:
		factor=0
	return {key:value*factor for key,value in d.iteritems()}




def compare_vector(file1,file2):
	vector1=normalize_vector(crea_vettore_comulato(file1))
	vector2=normalize_vector(crea_vettore_comulato(file2))
	
	result=0

	all_key=list(set().union(vector1.keys(),vector2.keys()))
        for k in all_key:
                result+=vector1.get(k,0)*vector2.get(k,0)
        return result
	
