import requests
from bs4 import BeautifulSoup
import pandas as pd
district_name=[]
commodity_name=[]
i=1
cstring=""
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
				if x==2:
					c=t.text[1:-1]
				elif x==3:
					d=t.text[1:-1]
				if x==3:					
					hi=t.find_all('span')
					hii=""
					for ii in hi:
						hii=ii.text
					d=t.text
					p=d.replace(hii,"")
					q="  -  "
					if q in p:
						gg=p.replace(q,"")
					cstring=cstring+gg[1:-1]
					d=cstring
					cstring=""
				x=x+1



		
			district_name.append((c))
			commodity_name.append((d))
		#print(a,b,c,d,e)
	i=i+1


df=pd.DataFrame(district_name, columns=['DistrictName'])
dff=pd.DataFrame(commodity_name,columns=['CommodityName'])
df.to_csv('DistrictName.csv',index=False,encoding='utf-8')
dff.to_csv('CommodityName.csv',index=False,encoding='utf-8')