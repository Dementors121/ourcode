
import  requests
from bs4 import BeautifulSoup
r=requests.get("http://agmarknet.nic.in/rep1newx1_today.asp")
soup=BeautifulSoup(r.content, "html.parser")
for link in soup.find_all("td",{"width":"20%"}):
    print(link.text)