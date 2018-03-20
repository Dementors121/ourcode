import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
yy=yesterday.strftime('%d-%b-%y')

commodity='potato'
district='ajmer'
modalprice=""
commodity=commodity.upper()
district=district.upper()
r=requests.get("http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=5&Tx_State=RJ&Tx_District=1&Tx_Market=0&DateFrom="+yy+"&DateTo="+yy+"&Fr_Date="+yy+"&To_Date="+yy+"&Tx_Trend=0&Tx_CommodityHead="+commodity+"&Tx_StateHead=Rajasthan&Tx_DistrictHead="+district+"&Tx_MarketHead=--Select--")

soup=BeautifulSoup(r.text,'html.parser')
tr=soup.find_all('tr')
records=[]
for link in tr:
	td=link.find_all('td')
	if len(td)>1:
		x=0
		a=b=c=d=""
		for t in td:
			if x==8:
				d=t.text[1:-1]
			x=x+1
		records.append((d))

print("The price of "+commodity+" in district "+district+" is rupees "+d+"/Quintal.")
