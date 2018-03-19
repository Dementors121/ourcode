
import  requests
from bs4 import BeautifulSoup
r=requests.get("https://www.flipkart.com/search?q=mobile&otracker=start&as-show=on&as=off")
soup=BeautifulSoup(r.content, "html.parser")
for link in soup.find_all("div",{"class":"_3wU53n"}):
    print(link.text)