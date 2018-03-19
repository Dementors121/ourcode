import requests
from bs4 import BeautifulSoup
import pandas as pd
records=[]
i=1
cstring=""
while  i<22:
	r=requests.get('https://www.mandiguru.co.in/daily-bhav/rajasthan?page='+str(i))
	soup=BeautifulSoup(r.text,'html.parser')
	tr=soup.find_all('tr')
	for link in tr:
		td=link.find_all('td')
		d=""
		x=0;
		if len(td)>1:
			for t in td:
				if x==3:
					d=t.text[1:-1]
					cstring=cstring+d+","
				x=x+1		
			records.append((d))
		#print(a,b,c,d,e)
	i=i+1

f=open('cstring.txt','w+')
f.write(cstring)
df=pd.DataFrame(records, columns=['Product_name'])
df.to_csv('commodities.csv',index=False,encoding='utf-8')