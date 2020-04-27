import csv
from bs4 import BeautifulSoup
import pandas as pd

class ReadData(object):
    
    def __init__(self):
        return
    
    def read_write_data(self,filename):
        with open(filename) as fnm:
            soup = BeautifulSoup(fnm,'lxml')
        senders=[]
        recievers=[]
        messages=[]
        for div in soup.findAll('div'):
            sender = div.find('div',attrs={'class':'sender'})
            reciever = div.find('div',attrs={'class':'reciever'})
            paragraph = div.find('p', attrs={'class':''})
            # print(paragraph)
            if sender:
                senders.append(sender.text)
                if paragraph:
                    messages.append(paragraph.text)
            
            if reciever:
                recievers.append(reciever.text)
                if paragraph:
                    messages.append(paragraph.text)

        df = pd.DataFrame({'Senders Name':senders,'Receivers Name':recievers, 'Messages': messages}) 
        df.to_csv('chat.csv', index=False, encoding='utf-8')