import os

def rinomina(p,q,d):
	l=q.split()
	if l:
		q=l[0]
	name="%s_%s.txt" %(q,d)
	try:
		os.remove(name)
	except OSError:
		pass
	os.rename(p,name)
