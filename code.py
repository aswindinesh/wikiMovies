#scrapes data from list of movies in alphabetic order
#from https://en.wikipedia.org/wiki/List_of_films:_numbers

#saves into data.csv

import requests
import csv
from bs4 import BeautifulSoup
def convert(lst): 
      return ' '.join(lst) 
      
name_letter=["numbers","A","B","C","D","E","F","G","H","I","J-K","L","M","N-O","P","Q-R","S","U-W","X-Z"]
for i in name_letter:
    url = "https://en.m.wikipedia.org/wiki/List_of_films:_{}".format(i)
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'lxml')
    print("\nFetching:{}\n".format(i))
    for tag in soup.find_all("li"):
        with open('./dataset/data.csv', 'a', newline='',encoding="utf-8") as file:
            writer = csv.writer(file)
            #print("{0}: {1}".format(tag.name, tag.text))
            movie=[]
            year = []
            for word in tag.text.split():
                if word[0]=='(' :
                    year.append(word[1:5])
                else:
                    movie.append(word)
            writer.writerow([convert(movie),convert(year)])