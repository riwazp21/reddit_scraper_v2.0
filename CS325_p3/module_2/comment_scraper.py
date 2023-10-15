"""
File Name: comment_scraper.py
Author: Riwaz Poudel
Input: File containing the html contents of the reddit link
Output: comments from the reddit link
Functionality
1. The function comment_scraper in this python file is imported in run.py 
2. The function comment_scraper takes the html content file as an argument
3. It uses the beautifulsoup library to scrape out all the comments from file(comments have a unique tag), and stores it in data_str
4. data_str is passed into a function file_storer, which will store the comments into a proper file in its destination at Data/processed
"""
from bs4 import BeautifulSoup
import sys
from module_3.file_storer import file_storer

def comment_scraper(file):
	with open(file,'r',encoding = 'utf-8') as f:
		html_content = f.read()
	data_str = ""
	commentNum = 0;
	soup = BeautifulSoup(html_content,'html.parser')
	#f = open("comment.txt","w")
	for item in soup.find_all("div",class_="usertext-body may-blank-within md-container"):
		if(commentNum != 0):
			data_str = data_str + item.get_text()	
			commentNum = commentNum + 1;
		commentNum = commentNum + 1;
		
		#f.write(data_str)
	#print(data_str)
	#f.write(data_str)
	#f.close()
	file_storer('B',data_str)	
