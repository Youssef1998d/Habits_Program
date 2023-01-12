import pandas as pd
from gmail_api import get
from datetime import date

def get_data():
    if __name__ == '__main__':
        get()
    f=str(date.today())+'.csv'
    data=str(date.today())+".csv"
    return pd.read_csv(f, delimiter=';')
import numpy as np

def get_spending(start, to):
    s, l = 0, {}
    for f in ("2023-01-"+str(x).zfill(2) for x in range(start,to+1)): 
        df = pd.read_csv(f+'.csv', delimiter=';')
        df['Number'].replace({np.nan:'0'}, inplace=True)
        spend = df[(df['Action']=='Spend')|(df['Action']=='Save')]
        l[f] = sum([float(x.replace(',','.') ) for x in spend['Number']])
        s += sum([float(x.replace(',','.') ) for x in spend['Number']])
    return {"Total":s, "Daily":l}

def get_savings():
    to = int(str(date.today()).split('-')[2])
    s=0
    for f in ("2023-01-"+str(x).zfill(2) for x in range(9,to+1)): 
        df = pd.read_csv(f+'.csv', delimiter=';')
        df['Number'].replace({np.nan:'0'}, inplace=True)
        save = df[(df['Action']=='Save')]
        s += sum([float(x.replace(',','.') ) for x in save['Number']])
    return s

def get_earning(to = int(str(date.today()).split('-')[2])):
    s=0
    for f in ("2023-01-"+str(x).zfill(2) for x in range(9,to+1)): 
        df = pd.read_csv(f+'.csv', delimiter=';')
        df['Number'].replace({np.nan:'0'}, inplace=True)
        save = df[(df['Action']=='Cash-in')]
        s += sum([float(x.replace(',','.') ) for x in save['Number']])
    return s

def get_balance(at = int(str(date.today()).split('-')[2])):
    return get_earning(at)-get_spending(9, at)['Total']

print(get_balance(at = 11))