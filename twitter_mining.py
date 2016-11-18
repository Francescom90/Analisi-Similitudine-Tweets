try:
    import json
except ImportError:
    import simplejson as json
import time
import os
import getDate
import sys
import rinomina

#importo i metodi necessari dalla libreria di twitter
import tweepy
from tweepy import OAuthHandler
import config
def miner(q,d,have_date):
	query=q
	last_id=float('inf')
	counter=1
	lingua='it'
	total=0
	data=d
	
	
	
	
	#definizione funzioni
	def process_or_store(tweet):
		with open('data.txt','a') as out:
			json.dump(tweet,out)
			out.write("\n")
			return tweet['id']

	def check_limit(query,last_id,lingua): #gestisce il limite di richieste
		#print "inizio funzione check_limit"
		try:
			return ricerca(query_c,last_id,lingua)
		except tweepy.RateLimitError:
			print("\n Limite raggiunto: attesa per riprendere la computazione")
			time.sleep(15*61)
			return [last_id,-1]
		except tweepy.TweepError:
			print("\n errore sconosciuto: aspetto 10 secondi e riprovo")
			time.sleep(10)
			return [last_id,-1]

	def ricerca(query,last_id,lang):
		l=100
		counter=0
		#print "ricerca"
		res=api.search(q=query, max_id=last_id-1, count=l, lang=lingua)

		for i in res:
			last_id=process_or_store(i._json)
			counter=counter+1
		return [last_id,counter]

	#inserisco i dati in un modulo di accesso
	auth=OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_secret)
    
	#uso il modulo di accesso per iniziare una connessione con la API di Twitter
	api=tweepy.API(auth)
	print "accesso alla API di Twitter effettuato:"
    
	#imposto la data ed ottengo la data successiva da usare come estremi per la ricerca
	if(have_date):
		data,data_before=getDate.getDate(d)
		query='%s since:%s until:%s' %(query,data,data_before)
	
	query='%s' %(query,)
	query_c=query
    
            
	while True:
		last_id,counter=check_limit(query,last_id,lingua)
		
		if counter>0:
			total=total+counter
			print "\n %s: proc=%s/%s Last ID=%s" % (query,counter,total,last_id)
		if counter==0:
			print "Letture possibili terminate"
			if(os.path.isfile("data.txt")):
				rinomina.rinomina("data.txt",query,data)
			break
