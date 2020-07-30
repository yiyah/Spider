import requests
from bs4 import BeautifulSoup
import os


mainPage = "https://www.biqukan.com/73_73450/"


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
    hostIP = "http://www.biqukan.com"
    for a_item in a_labels[12:]:
        chapter.append(a_item.string)
        chapter_Link.append(hostIP+a_item.get('href'))
    return title[0].text, chapter, chapter_Link


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
