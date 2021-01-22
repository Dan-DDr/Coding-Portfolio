import requests
from bs4 import BeautifulSoup
from csv import writer


url = "https://www.dictionary.com/e/word-of-the-day/"
fname = 'w_of_day.txt'

def get_words(pages):
    with open(fname,'w') as f:
        csv_writer = writer(f)
        csv_writer.writerow(['Word','Meaning','Date'])
        r = requests.get(url)
        page = 1
        while r.status_code == 200 and page <= pages:
            soup = BeautifulSoup(r.text,'html.parser')
            # getting the words, meanings and dates in a list
            words = [word.h1.get_text() for word in soup.select('.otd-item-headword__word')]
            meanings = [mean.p.find_next_sibling().get_text() for mean in soup.select('.otd-item-headword__pos')]
            dates = [date.div.get_text() for date in soup.select('.otd-item-headword__date')]
            
            # writing the data into csv file
            for i in range(len(words)):
                csv_writer.writerow([words[i],meanings[i],dates[i]])

            # getting the loadmore button and continue scraping until page is reached
            link = soup.find(class_='otd-item__load-more')['href']
            print(link)
            r = requests.get(link)
            page += 1

get_words(3)
