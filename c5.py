#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import csv
from multiprocessing import Process,Queue
from datetime import date,datetime
import getopt
import configparser
queue1=Queue()
queue2=Queue()
class Args(object):
    def __init__(self):
        self.args=sys.argv[1:]
    try:
        def getargs(self):
            opts,args=getopt.getopt(self.args,"C:c:d:o:h",["help"])
            for o, a in opts:
                if o in ("-h","--help"):
                    print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")
                else:
                    pass
            return opts
            print(opts)
        def getcityname(self):
            cityname=self.getargs()[0][1].upper()
            return cityname
        def getconfigfile(self):
            configfile=self.getargs()[1][1]
            return configfile
        def getuserdatafile(self):
            userdatafile=self.getargs()[2][1]
            return userdatafile
        def getsalaryfile(self):
            salaryfile=self.getargs()[3][1]
            return salaryfile
    except:
        print("ERROR!")
class Config(Args):
    try:
        def _read_config(self):
            config=configparser.ConfigParser()
            config.read(self.getconfigfile())
            if self.getcityname()=='':
                cityname="DEFAULT"
            else:
                cityname=self.getcityname()
            return config[cityname]
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
            queue1.put(userdata)
    except:
        print("ERROR!")
class IncomeTaxCalculator(Config,UserData):
    def calc_for_all_userdata(self):
        userdata=queue1.get()
        num=userdata[0]
        salary=userdata[1]
        insurance=[]
        income=[]
        tax=[]
        money=[]
        config=self._read_config()
        rate=float(config['YangLao'])+float(config['YiLiao'])+float(config['ShiYe'])+float(config['GongShang'])+float(config['ShengYu'])+float(config['GongJiJin'])
        JiShuL=float(config['JiShuL'])
        JiShuH=float(config['JiShuH'])
        for s in salary:
            s=float(s)
            if 0<=s<=JiShuL:
                insurance.append(0)
            elif JiShuL<s<=JiShuH:
                insurance.append(s*rate)            
            else:
                insurance.append(JiShuH*rate)
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
            time=datetime.now()
            result.append([n,s,i,t,m,datetime.strftime(time,'%Y-%m-%d %H:%M:%S')])
        queue2.put(result)
    def export(self,default='csv'):
        result=queue2.get()
        with open(self.getsalaryfile(),'w')as f:
            write=csv.writer(f)
            write.writerows(result)
    def main(self):
        Process(target=self._read_users_data).start()
        Process(target=self.calc_for_all_userdata).start()
        Process(target=self.export).start()
if __name__=='__main__':
    f=IncomeTaxCalculator()
    f.main()    
    
