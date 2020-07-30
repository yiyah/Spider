import requests
from bs4 import BeautifulSoup
import re


url = "https://www.biqukan.com/38_38836/497783246.html" 
# url = "http://www.biqukan.com/1_1094/5403177.html"

def parseBody(url):
    # step1. get html
    html = requests.get(url)
    # encoding
    html.encoding = "gb2312"

    # step2. parse html
    soup = BeautifulSoup(html.text, 'lxml')
    # 2.1 way1 to select the content
    # texts = soup.select("#content")
    # 2.1 way2 to select the content
    texts = soup.find_all('div', class_='showtxt')

    # step3. get the interest content
    # But now the content also have <div> and 
    # the content is in one line, so need to split multi line.
    texts = str(texts[0])
    texts = texts.replace('<br/>', '\n')

    # step4. parse string
    soup = BeautifulSoup(texts, 'lxml')
    texts = soup.find_all('div', class_='showtxt')
    return texts[0].text
    

def main():
    text = parseBody(url)
    with open("html.html", 'w') as f:
        f.write(text)


if __name__ == '__main__':
    main()
