import requests
from bs4 import BeautifulSoup
import pandas as pd


commodity='potato'
district='ajmer'
commodity=commodity.upper()
district=district.upper()
r=requests.get("https://www.mandiguru.co.in/daily-bhav/rajasthan?date_from=&date_to=&mandi="+district+"+%28F+%26+V%29&product="+commodity+"+&search=Search")

soup=BeautifulSoup(r.text,'html.parser')
tr=soup.find_all('tr')
records=[]
for link in tr:
	td=link.find_all('td')
	if len(td)>1:
		x=0
		a=b=c=d=""
		for t in td:
			if x==4:
				d=t.text[45:-1]
			x=x+1
		records.append((d))

print("The price of "+commodity+" in district "+district+" is "+d+".")
df=pd.DataFrame(records,columns=['Price'])
df.to_csv('input_both_output_only_price.csv',index=False,encoding='utf-8')
