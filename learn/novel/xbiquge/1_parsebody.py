import requests
from bs4 import BeautifulSoup


url = "https://www.xsbiquge.com/15_15338/8549128.html"


def main():
    # step1. get html
    html = requests.get(url)
    html.encoding = "utf-8"

    # step2. parse html
    soup = BeautifulSoup(html.text, 'lxml')
    texts = soup.find_all('div', id='content')

    # step3. Data cleaning
    texts = str(texts[0])
    texts = texts.replace("<br/>", "\n")
    soup = BeautifulSoup(texts, 'lxml')
    texts = soup.find_all('div', id='content')
    with open("html.html", 'w') as f:
        f.write(texts[0].text)


if __name__ == '__main__':
    main()
