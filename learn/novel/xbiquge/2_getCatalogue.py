import requests
from bs4 import BeautifulSoup


mainPage = "https://www.xsbiquge.com/15_15338/"


def getCatalogueAndLink(url):
    # declare chapter and it's link is a list
    chapter = []
    chapter_Link = []

    html = requests.get(url)
    html.encoding = 'utf-8'

    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.find_all('h1')
    texts = soup.find_all('div', id="list")
    texts = str(texts[0])
    soup = BeautifulSoup(texts, 'lxml')
    a_labels = soup.find_all('a')
    hostIP = "https://www.xsbiquge.com"
    for a_item in a_labels:
        chapter.append(a_item.string)
        chapter_Link.append(hostIP+a_item.get("href"))

    return title, chapter, chapter_Link


def main():
    title, chapter, chapter_Link = getCatalogueAndLink(mainPage)

    with open("html.html", 'w') as f:
        for i in range(len(chapter)):
            f.write("%s --> %s\n" % (chapter[i], chapter_Link[i]))


if __name__ == '__main__':
    main()
