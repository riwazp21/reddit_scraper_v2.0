"""
File Name: file_storer.py
Author: Riwaz Poudel
Input: A unique value that identifies whether it came from module_1 or module_2, and a string value to store in a file
Output: comment.txt, or content.txt at Data/raw or Data/processed
Functionality
1. The function file_storer is imported in comment_scraper.py and content_scraper.py inside module_1 and module_2 respectively
2. The function file_storer has two arguments topic and data
3. The value of topic will be A if the function is used in content_scraper.py. The value of data will be the raw html content. The function will store the data into a file called content.txt inside Data/raw directory
4. The value of topic will be B if the function is used in comment_scraper.py. The value of data will be the comments from the reddit link. The function will store the data into a file called comment.txt inside Data/processed directory

"""
import os

def file_storer(topic, data):
	if(topic == 'A'):
		output_path = os.path.join("Data","raw","content.txt")
		with open(output_path,"w") as f:
			f.write(data)
		print("Content file stored succesfully\n")
	if(topic == 'B'):
		output_path = os.path.join("Data","processed","comment.txt")
		with open(output_path,"w") as f:
			f.write(data)
		print("Comment file stored succesfully\n")		
