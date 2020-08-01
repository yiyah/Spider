import requests
from bs4 import BeautifulSoup
import os

mainPage = "https://www.xsbiquge.com/15_15338/"


def getCatalogueAndLink(url):
    # declare chapter and it's link is a list
    chapter = []
    chapter_Link = []

    # step1. get html
    html = requests.get(url)
    html.encoding = 'utf-8'

    # step2. parse html
    soup = BeautifulSoup(html.text, 'lxml')
    # get title
    title = soup.find_all('h1')
    # locate the chapter
    texts = soup.find_all('div', id="list")
    # parse the string which contained the chapter and it's link
    soup = BeautifulSoup(str(texts[0]), 'lxml')
    # find all a label as list
    a_labels = soup.find_all('a')

    # step3. save them 
    hostIP = "https://www.xsbiquge.com"
    for a_item in a_labels:
        chapter.append(a_item.string)
        chapter_Link.append(hostIP+a_item.get("href"))

    return title[0].text, chapter, chapter_Link


def parseBody(url):
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
    return texts[0].text


def downloadBook(title, chapter, content):
    filePath = title+"/"+chapter+'.txt'
    with open(filePath, 'w') as f:
        f.write(content)


def main():
    title, chapter, chapter_Link = getCatalogueAndLink(mainPage)
    if os.path.exists(title):
        os.system("rm {}/*".format(title))
    else:
        os.mkdir(title)
    for i in range(len(chapter)):
        content = parseBody(chapter_Link[i])
        downloadBook(title, chapter[i], content)
        print("Downloading: %0.3f%%" % (i/len(chapter)), end='\r')
    print("finish!")


if __name__ == '__main__':
    main()
