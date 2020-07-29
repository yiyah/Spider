import requests
from bs4 import BeautifulSoup


hostIP = "http://www.biqukan.com"
mainPage = "http://www.biqukan.com/1_1094/"


def main():
    html = requests.get(mainPage)
    html.encoding = 'gb2312'
    soup = BeautifulSoup(html.text, 'lxml')
    texts = soup.find_all('div', class_="listmain")
    texts = BeautifulSoup(str(texts[0]), 'lxml')
    a_labels = texts.find_all('a')
    with open("a_html.html", 'w') as f:
        for a_item in a_labels:
            href = hostIP+a_item.get('href')
            f.write("%s --> %s\n" % (a_item.string, href))


if __name__ == '__main__':
    main()
