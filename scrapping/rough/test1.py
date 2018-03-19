from selenium import webdriver
from selenium.webdriver.common.by import By
from contextlib import closing
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

with closing(webdriver.Chrome()) as driver:
	driver.get("google.com")
	page_source=driver.page_source
	soup=BeautifulSoup(page_source,"lxml"
		)