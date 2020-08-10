import requests
from bs4 import BeautifulSoup


url = 'https://www.dmzj.com/info/yaoshenji.html'


def getCatalogueAndLink(url):
    chapter = []
    chapterLink = []

    # step1: get html
    html = requests.get(url)

    # step2: parse
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.find_all('h1')[0].text
    ulList = soup.find_all('ul', class_='list_con_li autoHeight')
    soup = BeautifulSoup(str(ulList[1]), 'lxml')
    a_labelList = soup.find_all('a')
    for item in a_labelList:
        chapter.append(item.get('title'))
        chapterLink.append(item.get('href'))
    return title, chapter, chapterLink


def main():
    title, chapter, chapterLink = getCatalogueAndLink(url)
    # verification
    with open('%s.html' % title, 'w') as file:
        for i in range(len(chapter)):
            file.write(str(chapter[i])+'  -->  '+str(chapterLink[i])+'\n')


if __name__ == '__main__':
    main()
