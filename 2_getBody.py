import requests
from bs4 import BeautifulSoup
import re


url = "http://www.biqukan.com/1_1094/5403177.html"


def main():
    html = requests.get(url)
    
    html.encoding = "gb2312"
    print(html.text)
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.text)
    # 1. way1 to select the content
    # texts = soup.select("#content")
    # 2. way2 to select the content
    texts = soup.find_all('div', class_='showtxt')
    # print(texts)
    # print(texts[0].text.replace('\xa0'*8, '\n1'))
    # texts = texts[0].text.replace(' \xa0'*8, '\n\n')
    # print(texts)


if __name__ == '__main__':
    main()
