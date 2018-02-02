#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys,getopt
import csv
from multiprocessing import Process,Queue
import ConfigParser
from datetime import date,datetime 
queue1=Queue()
queue2=Queue()
opts=getopt.getopt(sys.argv[1:],"hC:c:d:o:",["help"])
    for a,b in opts:
        if a in ('-h','--help'):
            print('Usage: calculator.py -C cityname -c configfile -d useredata -o resultdata')
            sys.exit()
        else:
            pass
class Config(self):
    def 
    try:
        configname=self.getargs()[0][1][1]
        def _read_config(self):
            config=ConfigParser.ConfigParser()
            config.read(configname)
            if self.getargs()[0][0][1]=='':
                city=DEFAULT
            else:
                city=self.getargs()[0][1][1].upper()
            JiShuL=float(config.get(city,"JishuL"))
            JiShuH=float(config.get(city,"JishuH"))
            rate=float(config.get(city,"YangLao"))+float(config.get(city,"YiLiao"))+float(config.get(city,"ShiYe"))+float(config.get(city,"GongShang"))+float(config.get(city,"ShengYu"))+float(config.get(city,"GongJiJin"))
            return JiShuL,JiShuH,rate

    except:
        print("ERROR!")
    
class UserData(Args):
    try:
        def _read_users_data(self):
            userdata=[]
            a=[]
            b=[]
            c=[]
            with open(self.getargs()[0][2][1]) as file:
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
        for s in salary:
            s=float(s)
            if 0<=s<=self._read_config()[0]:
                insurance.append(0)
            elif self._read_config()[0]<s<=self._read_config()[1]:
                insurance.append(s*self._read_config()[2])            
            else:
                insurance.append(self._read_config()[1]*self._read_config()[2])
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
            time =datetime.now()
            result.append([n,s,i,t,m,datetime.strftime(time,'%Y%m%d %H%M%S')])
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
    
