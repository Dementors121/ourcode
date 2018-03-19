import pandas as pd
import requests
from bs4 import BeautifulSoup
url="https://www.mandiguru.co.in/daily-bhav/rajasthan?page=1"
data=pd.read_html(url,header=0)

print(data[0])