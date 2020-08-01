import requests
from bs4 import BeautifulSoup


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


def main():
    title, chapter, chapter_Link = getCatalogueAndLink(mainPage)

    with open(title+".html", 'w') as f:
        for i in range(len(chapter)):
            f.write("%s --> %s\n" % (chapter[i], chapter_Link[i]))


if __name__ == '__main__':
    main()
