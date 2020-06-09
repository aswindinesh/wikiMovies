#scrapes list of movie and their corresponding year of release between 1986 to 2029(unreleased)
#results in a messy dataset, all td are included

#saves into movie_yearwise.csv
import requests
import csv
from bs4 import BeautifulSoup
def convert(lst): 
      return ' '.join(lst) 
      
film_region=["American","Bangladeshi","British","Canadian","Chinese","Filipino","Assamese","Indian_Bengali","Bollywood","Kannada","Gujarati","Malayalam","Marathi","Punjabi","Tamil","Telugu","Tulu","Japanese","Russian","Australian"]
#1879-2020
#1897-japanese
for year in range(1986,2029):
    print("\nFetching:{}\n".format(year))
    for j in film_region:
        url = "https://en.m.wikipedia.org/wiki/List_of_{}_films_of_{}".format(j,year)
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')
        print("\nFetching:{}\n".format(j))
        for tag in soup.find_all("td"):
            with open('./dataset/movie_yearwise.csv', 'a', newline='',encoding="utf-8") as file:
                writer = csv.writer(file)
                #print("{0}: {1}".format(tag.name, tag.text))
                movie=[]
                for word in tag.text.split():
                    movie.append(word)
                writer.writerow([convert(movie),year])