import sys
import datetime

def getDate(inp):
    giorno,mese,anno=split=inp.split("-",3)
    data=datetime.date(int(anno),int(mese),int(giorno))
    data_prima=data+datetime.timedelta(days=1)
    
    return [data,data_prima]
