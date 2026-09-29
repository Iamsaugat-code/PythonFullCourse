

# Web scraping in multithreading:
# It means using multiple threads to collect data from
# different web pages at the same time, making web scraping faster


# https://www.ibm.com/think/topics/ai-agent-protocols#1509394340
# https://www.ibm.com/think/topics/agentic-ai#2095054954
# https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai#7281538


import threading
from bs4 import BeautifulSoup
import requests


urls = [
    'https://www.ibm.com/think/topics/ai-agent-protocols#1509394340',
    'https://www.ibm.com/think/topics/agentic-ai#2095054954',
    'https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai#7281538'
]



def fetch_content(url):
    respone = requests.get(url)
    soup = BeautifulSoup(respone.content,'html.parser')
    print(f"len of content : {len(soup.text)} from the urls {url}")



threads = []

for i in urls:
    thread = threading.Thread(target=fetch_content,args=(i,))
    threads.append(thread)
    thread.start()

for i in threads:
    thread.join()
    
    
    
    
    
# Your code uses soul, but normally we use the name soup.

# response.content → gets the webpage's HTML content.
# BeautifulSoup() → reads and parses the HTML.
# 'html.parser' → tells BeautifulSoup which parser to use.

    
