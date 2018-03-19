import requests
from bs4 import BeautifulSoup
import pandas as pd


commodity='potato'
commodity=commodity.upper()
r=requests.get("https://www.mandiguru.co.in/daily-bhav/rajasthan?product="+commodity+"&search=search")

soup=BeautifulSoup(r.text,'html.parser')
tr=soup.find_all('tr')
records=[]
for link in tr:
	td=link.find_all('td')
	if len(td)>1:
		x=0
		a=b=c=d=""
		for t in td:
			if x==0:
				a=t.text;
			elif x==1:
				b=t.text
			elif x==2:
				c=t.text[1:-1]
			elif x==4:
				d=t.text[45:-1]
			else:
				e=t.text
			x=x+1
		records.append((a,b,c,d))

df=pd.DataFrame(records,columns=['Sl_no','Date','Place','Price'])
df.to_csv('commodity_search.csv',index=False,encoding='utf-8')
