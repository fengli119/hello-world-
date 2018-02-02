#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import csv
class Args(object):
    def __init__(self):
        self.args=sys.argv[1:]
    try:
        def getconfigfile(self):
            index=self.args.index('-c')
            configfile=self.args[index+1]
            return configfile
        def getuserdatafile(self):
            index=self.args.index('-d')
            userdatafile=self.args[index+1]
            return userdatafile
        def getsalaryfile(self):
            index=self.args.index('-o')
            salaryfile=self.args[index+1]
            return salaryfile
    except:
        print("ERROR!")
class Config(Args):
    try:
        def _read_config(self):
            a=[]
            config=dict()
            with open(self.getconfigfile()) as file:
                for x in file:
                    a.append(x.strip())
                for i in a :
                    num=i.split()[0]
                    config[num]=float(i.split()[2])
            return config
    except:
        print("ERROR!")
    
class UserData(Args):
    try:
        def _read_users_data(self):
            userdata=[]
            a=[]
            b=[]
            c=[]
            with open(self.getuserdatafile()) as file:
                for x in file:
                    a.append(x.strip())
                for i in a:
                    b.append(i.split(",")[0])
                    c.append(i.split(",")[1])
                b=tuple(b)
                c=tuple(c)
                userdata=[b,c]
            return userdata
    except:
        print("ERROR!")
class IncomeTaxCalculator(Config,UserData):
    def calc_for_all_userdata(self):
        num=self._read_users_data()[0]
        salary=self._read_users_data()[1]
        insurance=[]
        income=[]
        tax=[]
        money=[]
        config=self._read_config()
        rate=config['YangLao']+config['YiLiao']+config['ShiYe']+config['GongShang']+config['ShengYu']+config['GongJiJin']
        for s in salary:
            s=float(s)
            if 0<=s<=2193.00:
                insurance.append(0)
            elif 2193.00<s<=16446.00:
                insurance.append(s*rate)            
            else:
                insurance.append(16446.00*rate)
        for s,i  in zip(salary,insurance):
            s=float(s)
            i=float(i)
            income.append(s-i-3500)
        for i in income:
            i=float(i)
            if i<=0:
                tax.append(0)
            elif 0<i<=1500:
                tax.append(i*0.03)
            elif 1500<i<=4500:
                tax.append(i*0.1-105)
            elif 4500<i<=9000:
                tax.append(i*0.2-555)
            elif 9000<i<=35000:
                tax.append(i*0.25-1005)
            elif 35000<i<=55000:
                tax.append(i*0.3-2755)
            elif 55000<i<=80000:
                tax.append(i*0.35-5500)
            else:
                tax.append(i*0.45-13505)
        for s,i,t in zip(salary,insurance,tax):
            s=float(s)
            i=float(i)
            t=float(t)
            money.append(s-i-t)
        result=[]
        for n,s,i,t,m in zip(num,salary,insurance,tax,money):
            i=format(float(i),".2f")
            t=format(float(t),".2f")
            m=format(float(m),".2f")
            result.append([n,s,i,t,m])
        return result
    def export(self,default='csv'):
        result=self.calc_for_all_userdata()
        with open(self.getsalaryfile(),'w')as f:
            write=csv.writer(f)
            write.writerows(result)
if __name__=='__main__':
    f=IncomeTaxCalculator()
    f.export()


