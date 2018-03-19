
import  requests
from bs4 import BeautifulSoup
r=requests.get("http://agmarknet.nic.in/rep1newx1_today.asp")
soup=BeautifulSoup(r.content, "html.parser")
pname=[]
man=[]
minn=[]
trr=soup.find_all("td",attrs={"width":"50%"},{"color":"#000080"})
for link in trr:
    pname.append(link.text[1:-1])
trr=soup.find_all("td",attrs={"width":"20%"},{"color":"#000080"})
x=0;
for link in trr:
	if x%2==0:
		man.append(link.text[1:-1])
	else:
		minn.append(link.text[1:-1])
	x=x+1
record=[]
#print(str(len(pname))+" "+str(len(man))+" "+str(len(minn)))
for x in range(0,len(pname)):
	aa=pname[x]
	bb=man[x]
	cc=minn[x]
	record.append((aa,bb,cc))


#for x in record[0:10]:
#	print(x[1])
import pandas as pd
df=pd.DataFrame(record, columns=['pulse_name','max_price','min_price'])
df.to_csv('agri.csv',index=False,encoding='utf-8')