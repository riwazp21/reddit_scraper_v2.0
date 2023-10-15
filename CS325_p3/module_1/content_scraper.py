'''
File Name: content_scraper.py
Author: Riwaz Poudel
Input: reddit url
Output: raw html data
Functionality
1. The function content_scraper in this python file is imported in run.py 
2. The function content_scraper takes the reddit url
3. It uses the beautifulsoup library to scrape out all the html contents of the file and stores it in htmldata
4. htmldata is passed into a function file_storer, which will store the content into a proper file in its Destination Data/raw

'''
import requests
from bs4 import BeautifulSoup
import sys
from module_3.file_storer import file_storer
def content_scraper(url):
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
	r = requests.get(url,headers=headers)
	#f = open("content.txt","w")
	htmldata = r.text
	data_str = ""
	soup = BeautifulSoup(htmldata, 'html.parser')
	file_storer('A',htmldata)
	
