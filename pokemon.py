import requests
from bs4 import BeautifulSoup
import csv


def main():
    url = 'https://www.pokemon.co.jp/info/2019/08/190816_gm01.html?i002=news'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')

    sponsors = soup.find_all("div", attrs={"class": "p-pagepnl__i-tbl"})

    csvlist = []

    for sponsor in sponsors:
        news_txt = sponsor.text.strip()
        csvlist.append([news_txt])

    return csvlist


    def write():
        return csvlist
        output_file = open('pokemon.csv', 'w')
        output_writer = csv.writer(output_file)
        output_writer.writerows(csvlist)
        output_file.close()
    write()

if __name__ == '__main__':

    main()



