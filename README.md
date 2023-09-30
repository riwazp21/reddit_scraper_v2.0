# Project - 1 CS 325 Riwaz Poudel
## Python Program to scrape comments from a reddit post
### Description
This project scraps all the user comments from a reddit post and stores in it a file.
### How to make this program run in your device?
#### Installing Anaconda in your device
1. You would need to install Anaconda into your device. Head to anaconda.com and install the latest version of Anaconda to your device.
2. After you have installed the Anaconda, you can check if it was succesfully installed or not by running the following command in your terminal. Mac users can use their terminal whereas Windows user can do this step in the Anaconda terminal. 
   ```conda activate```
#### Cloning the Project in your device
1. In this github repository, click the green button that says Code.
2. You can see a HTTPS link, copy that to your clipboard.
3. In your terminal, go to your desired folder, where you want to clone this repository
4. Type the following line of code to your terminal
   ```git clone "Paste the HTTPS link you copied earlier, don't include the quotation"```
5. After this command, a local file in your device exists
#### Setting up the conda environment
1. In your terminal change your directory to go inside the reddit_scraper project file
2. The project file(reddit_scrapper) has three files
   ```
   README.md (README document)
   requirement.yaml (yaml file)
   scrappy.py (main code)
   comments.txt (sample output from the code after it was ran on the given input in the project document)
   ```
3. The requirement.yaml file has all the necessary packages for this code to work
4. To create a new environment, run the following code in your terminal, env_name can be anything. Make sure its unique and somethign you have never used before
   ```conda env create --name env_name --file=requirement.yml```
5. This will take few minutes. After succesful activation, run the following code in your terminal. env_name is the name of environment you initialized in previous step
   ```conda activate env_name```
#### Running the program
   1. To run the python program, run the following command in your terminal
      ```python scrappy.py URL```
   2. Always make sure you have your environment working before you run your python script.
   3. For example,
      ```python scrappy.py https://www.reddit.com/r/funny/comments/16brnzb/self_aware/```
   4. This will take few minutes, depending on how big the reddit post is.
   5. All the comments are stored in the comment.txt file in the same directory as your project
   6. To see all the comments and replies, run the following code in your teminal
      ```cat comment.txt```
   
