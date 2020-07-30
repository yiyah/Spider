import requests
from bs4 import BeautifulSoup
import os

hostIP = "http://www.biqukan.com"
mainPage = "http://www.biqukan.com/1_1094/"


def getCatalogueAndLink(url):
    # declare chapter and it's link is a list
    chapter = []
    chapter_Link = []
    # step1. get html
    html = requests.get(url)
    html.encoding = 'gb2312'
    
    # step2. parse html
    soup = BeautifulSoup(html.text, 'lxml')
    # get title
    title = soup.find_all('h2')
    # locate the chapter
    texts = soup.find_all('div', class_="listmain")
    # parse the string which contained the chapter and it's link
    texts = BeautifulSoup(str(texts[0]), 'lxml')
    # find all a label as list
    a_labels = texts.find_all('a')
    
    # step3. save them and skip the front chapter
    for a_item in a_labels[13:]:
        chapter.append(a_item.string)
        chapter_Link.append(hostIP+a_item.get('href'))
    return title[0].text, chapter, chapter_Link


def main():
    title, chapter, chapter_Link = getCatalogueAndLink(mainPage)
    with open(title+".html", 'w') as f:
        for i in range(len(chapter)):
            f.write("%s --> %s\n" % (chapter[i], chapter_Link[i]))


if __name__ == '__main__':
    main()
