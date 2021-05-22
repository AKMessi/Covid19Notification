from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title = title, 
        message = message,
        # app_icon = "C:/Users/Aaryan/Desktop/Coding/Python Codes/COVID 19 Notification/icon.ico",
        timeout = 60
    )

def getData(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    # notifyMe("Aaryan", "Covid-19 Cases In India")
    myHtmlData = getData('https://www.worldometers.info/coronavirus/')
    # print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())
    myDatastr = " "
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDatastr += tr.get_text()
    myDatastr = myDatastr[0:]
    itemList = myDatastr.split("\n\n")
    
    states = ['2']
    for item in itemList[0:100]:
        dataList = item.split("\n")
        if dataList[0] in states:
            print(dataList)
            nTitle = 'Cases of COVID 19 in India'
            nText = f"Total Cases : {dataList[2]}"
            notifyMe(nTitle, nText)
