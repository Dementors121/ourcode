import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

soup=BeautifulSoup(r.text,'html.parser')
#print(r.text[0:500])

results=soup.find_all('span',attrs={'class':'short-desc'})
records=[]

for result in results:
	date=result.find('strong').text[0:-1]+', 2017'
	lie=result.contents[1][1:-2]
	explanation=result.find('a').text[1:-1]
	url=result.find('a')['href']
	records.append((date,lie,explanation,url))


import pandas as pd
df=pd.DataFrame(records,columns=['date','lie','explanation','url'])
df['date']=pd.to_datetime(df['date'])
df.to_csv('trumps_lies.csv',index=True,encoding='utf-8')