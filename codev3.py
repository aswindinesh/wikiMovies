#scapes tables of data of movies between 1986 to 2021
#before 1986, list of names
from bs4 import BeautifulSoup
import requests
import os
import codecs
import time

film_region=["American","Bangladeshi","British","Canadian","Chinese","Filipino","Assamese","Indian_Bengali","Bollywood","Kannada","Gujarati","Malayalam","Marathi","Punjabi","Tamil","Telugu","Tulu","Japanese","Russian","Australian"]

for year in range(1986,2029):
    for j in film_region:
        wiki = "https://en.m.wikipedia.org/wiki/List_of_{}_films_of_{}".format(j,year)
        header = {
            'User-Agent': 'Mozilla/5.0'
        }  # Needed to prevent 403 error on Wikipedia
        page = requests.get(wiki, headers=header,timeout=20)
        soup = BeautifulSoup(page.text, 'lxml')

        tables = soup.findAll("table", {"class": "wikitable"})
        page = os.path.split(wiki)[1]
        
        os.mkdir("./{}".format(page))
        
        for tn, table in enumerate(tables):

            rows = table.findAll("tr")
            row_lengths = [len(r.findAll(['th', 'td'])) for r in rows]
            ncols = max(row_lengths)
            nrows = len(rows)
            data = []
            for i in range(nrows):
                rowD = []
                for j in range(ncols):
                    rowD.append('')
                data.append(rowD)

            for i in range(len(rows)):
                row = rows[i]
                rowD = []
                cells = row.findAll(["td", "th"])
                for j in range(len(cells)):
                    cell = cells[j]

                    cspan = int(cell.get('colspan', 1))
                    rspan = int(cell.get('rowspan', 1))
                    l = 0
                    for k in range(rspan):
                        while data[i + k][j + l]:
                            l += 1
                        for m in range(cspan):
                            cell_n = j + l + m
                            row_n = i + k
                            cell_n = min(cell_n, len(data[row_n])-1)
                            data[row_n][cell_n] += cell.text

                data.append(rowD)
        
            fname = './{}/output_{}_t{}.csv'.format(page,page, tn)
            f = codecs.open(fname, 'w',encoding="utf-8")
            for i in range(nrows):
                rowStr = '\t'.join(data[i])
                rowStr = rowStr.replace('\n', '')
                #print(rowStr)
                f.write(rowStr + '\n')

            f.close()
    time.sleep(5)
time.sleep(30)