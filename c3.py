#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import csv
class Args(object):
    def __init__(self):
        self.args=sys.argv[1:]
    try:
        def getconfigfile:
            index=args.index('-c')
            configfile=args[index+1]
            return configfile
        def getuserdatafile:
            index=args.index('-d')
            userdatafile=args[index+1]
            return userdatafile
        def getsalaryfile:
            index=args.index('-o')
            salaryfile=args[index+1]
            return salaryfile
    except:
        print("ERROR!")
class Config(object):
    def __init__(self):
        self.config=self._read_config()
    def _read_config(self):
    a=[]
    config=dict()
    with open Args(self).getconfigfile() as file:
        for x in file:
            a.append(x.strip())
        for i in a :
            num=i.split()[0]
            config[num]=i.split()[2]
class UserData(object):
    def __init__(self):
        self.userdata=self._read_users_data()
    def _read_users_data(self):
        userdata=[]
        a=[]
        b=[]
        c=[]
        with open Args(self).getuserdatafile as file:
            for x in file:
                a.append(x.strip())
            for i in a:
                b.append(a.split(",")[0]
                c.append(a.split(",")[1]
            b=tuple(b)
            c=tuple(c)
            userdata=[b,c]

class IncomeTaxCalculator(object):
    def calc_for_all_userdata(self):
        num=UserData(self)._read_uesr_data()[0]
        salary=UserData(self)._read_user_data()[1]
        if 0<salary<=2193.00:
            insurance=0
        elif 2193.00 <salary<=16446.00:
            insurance=salary*
        else salary>16446.00:
            insurance=16446.00*
        tax
        income=
        return [num,sallary,insurance,tax,income]
    def export(self,default='csv'):
        result=self.calc_for_all_userdata()
        with open("")as f:
            write=csv.writer(f)
            write.writerows(result)
if __name__=='__main__':

