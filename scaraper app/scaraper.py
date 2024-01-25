import requests
from bs4 import BeautifulSoup 
from transformers import pipeline


#url=(r"https://www.flipkart.com/steeloart-new-cradle-silver-metaalic-beautiful-pink-buggy/p/itm86d89f3254ef5?pid=STRGBNAWXGG3HYD3&lid=LSTSTRGBNAWXGG3HYD3T82HOI&marketplace=FLIPKART&q=kids&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=en_zrIl-gQesmGhx5p2KK_kNnnZFCy1vL48wyYtT5AYGQoTvMn8_XrxkUtou0EXW1MD3VTe9GLiWh1aFY1l8KilGg%3D%3D&ppt=sp&ppn=sp&ssid=vefniaducg0000001706101973219&qH=d2466bd5a5facbe6") #url of site optimized for flipkart

bart = pipeline("summarization",model="sshleifer/distilbart-cnn-12-6",truncation=True)

def get_content(site):
    r = requests.get(site) #getting html
    #print(r)
    soup = BeautifulSoup(r.content, 'lxml')
    #print(soup.text+"\n\n")
    description=bart(soup.text)
    #print(description[0]['summary_text'])
    return description[0]['summary_text']



#get_content(url)