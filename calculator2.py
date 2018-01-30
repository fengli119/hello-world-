#!/usr/bin/env python3

import sys
taxdict=dict()
try:
    for arg in sys.argv[1:]:
        num=int(arg.split(':')[0])
        taxdict[num]=int(arg.split(':')[1])
except:
    print("Parameter Error")
def tax_calculator(num,salary):
    income=salary*(1-0.08-0.02-0.005-0.06)-3500
    if income<=0:
        tax=0
    elif 0<income<=1500:
        tax=income*0.03
    elif 1500<income<=4500:
        tax=income*0.1-105
    elif 4500<income<=9000:
        tax=income*0.2-555
    elif 9000<income<=35000:
        tax=income*0.25-1005
    elif 35000<income<=55000:
        tax=income*0.3-2755
    elif 55000<income<=80000:
        tax=income*0.35-5505
    else:
        tax=income*0.45-13505
    print(num,format((salary*(1-0.08-0.02-0.005-0.06)-tax),".2f"),sep=":")
if __name__=="__main__":
    taxdict=sorted(taxdict.keys())
    for key,value in taxdict.items():
        tax_calculator(key,value)
    

    
