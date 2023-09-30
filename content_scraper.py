import requests
from bs4 import BeautifulSoup
import sys

def content_scraper(url):
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
	r = requests.get(url,headers=headers)
	#f = open("content.txt","w")
	htmldata = r.text
	data_str = ""
	soup = BeautifulSoup(htmldata, 'html.parser')
	with open('content.txt','w') as f:
		f.write(htmldata)
	


		
	
if __name__ == "__main__":
	url = sys.argv[1]
	print(url)
	content_scraper(url)
	
	
