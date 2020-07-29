import requests
from bs4 import BeautifulSoup
import os


hostIP = "http://www.biqukan.com"
mainPage = "http://www.biqukan.com/1_1094/"


def getCatalogueAndLink(url):
    chapter = []
    chapter_Link = []
    html = requests.get(url)
    html.encoding = 'gb2312'
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.find_all('h2')
    texts = soup.find_all('div', class_="listmain")
    texts = BeautifulSoup(str(texts[0]), 'lxml')
    
    a_labels = texts.find_all('a')
    for a_item in a_labels[13:]:
        chapter.append(a_item.string)
        chapter_Link.append(hostIP+a_item.get('href'))
    return title[0].text, chapter, chapter_Link


def parseBody(url):
    html = requests.get(url)
    html.encoding = "gb2312"
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.text)
    # 1. way1 to select the content
    # texts = soup.select("#content")
    # 2. way2 to select the content
    texts = soup.find_all('div', class_='showtxt')
    return texts[0].text.replace('\xa0'*8, '\n'+'\xa0'*2)


def downloadBook(title, chapter, content):
    filePath = title+"/"+chapter+'.txt'
    with open(filePath, 'w') as f:
        f.write(content)


def main():
    title, chapter, chapter_Link = getCatalogueAndLink(mainPage)
    os.makedirs(title)
    for i in range(len(chapter)):
        content = parseBody(chapter_Link[i])
        downloadBook(title, chapter[i], content)
        print("Downloading: %0.3f%%" % (i/len(chapter)), end='\r')
    print("finish!")


if __name__ == '__main__':
    main()
