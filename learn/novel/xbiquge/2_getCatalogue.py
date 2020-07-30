import requests
from bs4 import BeautifulSoup


mainPage = "https://www.xsbiquge.com/15_15338/"


def getCatalogueAndLink(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    texts = soup.find_all('div', id="list")
    texts = str(texts[0])
    soup = BeautifulSoup(texts)
    texts = soup.find_all('a')
    with open("html.html", 'w') as f:
        f.write(texts)


def main():
    getCatalogueAndLink(mainPage)


if __name__ == '__main__':
    main()