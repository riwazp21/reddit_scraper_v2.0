"""
File Name: run.py
Author: Riwaz Poudel
Input: reddit URL through command line argument
Output: content.txt and comment.txt inside Data/Raw and inside Data/Processed respectively
Functionality:
1. This is the main file of the entire program. 
2. This file receives the reddit link through the command line argument
3. The file imports the function content_scraper and comment_scraper from module 1 and module 2
4. The reddit link is passed through the content_scraper
5. The raw file is passed through the comment_scraper
6. The output from this file would be both the raw and processed file of the reddit link that includes html content, and the comments

Basic structure of how the modules work and interact with each other
CS325_p3/
|--run.py
|--module_1
|   └──content_scraper.py
|--module_2
|	└──comment_scraper.py
|--module_3
	└──file_storer.py
run.py calls functions content_scraper and comment_scraper from module 1 and module 2
content_scraper.py(module_1) and comment_scraper.py(module_2) calls file_storer.py from module_3

"""
from bs4 import BeautifulSoup
from module_1.content_scraper import content_scraper
from module_2.comment_scraper import comment_scraper
import sys
import os

if __name__ == "__main__":
	url = sys.argv[1]
	content_scraper(url)
	content_path = os.path.join("Data","raw","content.txt")
	comment_scraper(content_path)

