import requests
from bs4 import BeautifulSoup
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
					hi=t.find_all('span')
					hii=""
					for ii in hi:
						hii=ii.text
					d=t.text
					p=d.replace(hii,"")
					q="  -  "
					if q in p:
						gg=p.replace(q,",")
					cstring=cstring+gg[1:-1]
				x=x+1		
		#print(a,b,c,d,e)
	i=i+1

f=open('cstring_hindi_replaced.txt','w+')
f.write(cstring)