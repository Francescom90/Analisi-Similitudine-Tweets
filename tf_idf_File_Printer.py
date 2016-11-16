from __future__ import division, unicode_literals
import math
from textblob import TextBlob as tb
import my_utility
import sys


def tf(word, blob):
    #print "tf\n"
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    #print "n_containing\n"
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    #print "idf\n"
	result= math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
	if result<=0:
		return 0
	return result

def tfidf(word, blob, bloblist):
    #print "tfidf\n"
    a=tf(word, blob)
    b=idf(word, bloblist)
    #print "Su %s TF=%s e IDF=%s"%(word,a,b)
    return  a*b 

def tfidf_run(nome_file):
	nome_out="rated token/"
	temp_list=""
	bloblist=[]
	#sys.stdout=open("log.txt","w")
	
	print "Avvio tf-idf"
	#per il calcolo dei singoli tweet come singoli documenti
	
	print nome_file
	list_tweet=my_utility.parse_tweet_file(nome_file)
	#print list_tweet
	for elem in list_tweet:
		bloblist.append(tb(elem))    
	#nome_file=num
	
	print "______________"
	print "______________"
	
	for i, blob in enumerate(bloblist):
		print("Top words in document {}".format(i + 1))
		scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		complete="%s%s"%(nome_out,nome_file)
		with open(complete,"a") as out:
			for word, score in sorted_words[:50]:
				#print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
				out.write("%s:%s "%(word,round(score,5)))
			out.write("\n")
	return complete