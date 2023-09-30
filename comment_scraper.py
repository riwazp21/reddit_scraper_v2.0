from bs4 import BeautifulSoup
import sys

def comment_scraper(file):
	with open(file,'r',encoding = 'utf-8') as f:
		html_content = f.read()
	data_str = ""
	commentNum = 0;
	soup = BeautifulSoup(html_content,'html.parser')
	f = open("comment.txt","w")
	for item in soup.find_all("div",class_="usertext-body may-blank-within md-container"):
		if(commentNum != 0):
			data_str = data_str + item.get_text()	
			commentNum = commentNum + 1;
		commentNum = commentNum + 1;
		
		#f.write(data_str)
	#print(data_str)
	f.write(data_str)
	f.close()	
		
	
if __name__ == "__main__":
	file_name = sys.argv[1]
	print(file_name)
	
	comment_scraper(file_name)
