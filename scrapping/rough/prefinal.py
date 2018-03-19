import requests
from bs4 import BeautifulSoup
import pandas as pd
records=[]
i=1
while  i<22:
	r=requests.get('https://www.mandiguru.co.in/daily-bhav/rajasthan?page='+str(i))
	soup=BeautifulSoup(r.text,'html.parser')
	tr=soup.find_all('tr')
	for link in tr:
		td=link.find_all('td')
		a=b=c=d=e=""
		x=0;
		if len(td)>1:
			for t in td:
				if x==0:
					a=t.text
				elif x==1:
					b=t.text
				elif x==2:
					c=t.text[1:-1]
				elif x==3:
					d=t.text[1:-1]
				else:
					e=t.text[45:-1]
				x=x+1



		
		records.append((a,b,c,d,e))
		#print(a,b,c,d,e)
	i=i+1


df=pd.DataFrame(records, columns=['sl_no','date','Name','Product_name','price'])

df.to_csv('agriprefinal.csv',index=False,encoding='utf-8')