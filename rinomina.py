import os

def rinomina(p,q,d):
    l=q.split()
    if l:
        q=l[0]
    name="%s_%s.txt" %(q,d)
    #print name
    os.rename(p,name)
