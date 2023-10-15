# Project - 3 CS 325 Riwaz Poudel
## Python Program to scrape comments from a reddit post using modules
### Description
This project scraps all the user comments from a reddit post and stores in it a file.
### How to make this program run in your device?
#### Installing Anaconda in your device
1. You would need to install Anaconda into your device. Head to anaconda.com and install the latest version of Anaconda to your device.
2. After you have installed the Anaconda, you can check if it was succesfully installed or not by running the following command in your terminal. Mac users can use their terminal whereas Windows user can do this step in the Anaconda python terminal. 
   ```conda activate```
#### Cloning the Project in your device
1. In this github repository, click the green button that says Code.
2. Make sure you are in the modular branch
3. You can see a HTTPS link, copy that to your clipboard.
4. In your terminal, go to your desired folder, where you want to clone this repository
5. Type the following line of code to your terminal
   ```git clone "Paste the HTTPS link you copied earlier, don't include the quotation"```
6. After this command, a local file in your device exists
#### Setting up the conda environment
1. In your terminal change your directory to go inside the reddit_scraper_v2.0 project file. 
2. The project file(reddit_scrapper_v2.0) has the following files
   ```
   README.md (README document)
   requirement.yaml (yaml file)
   content_scraper.py(Python code that will scrape all the html content from a reddit link and dump it into a file)
   comment_scraper.py(Python code that will scrape all the comments from a given dump file that contains all the html content)
   content.txt(sample html dump file after running content_scraper.py)
   comments.txt (sample dump file after running comment_scraper.py)
   README.md(this file)
   CS325_p3 folder(This is the main project file)
   
   ```
3. The requirement.yaml file has all the necessary packages for this code to work
4. To create a new environment, run the following code in your terminal, env_name can be anything. Make sure its unique and something you have never used before
   ```conda env create --name env_name --file=requirement.yml```
5. This will take few minutes. After succesful activation, run the following code in your terminal. env_name is the name of environment you initialized in previous step
   ```conda activate env_name```
#### Running the program
   
   1. Make sure you have your environment working before you run your python script.
   2. Go to CS325_p3 director
   3. Run the following command to run the project
      ```python run.py URL```
   4. For example,
      
      ```python run.py https://www.old.reddit.com/r/funny/comments/16brnzb/self_aware/```
   6. After running this line of code, you will have a new file called content.txt inside the Data/raw directory, which has all the html content of the given link. And another file called comment.txt inside the Data/processed directory
   
      
