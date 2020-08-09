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
    ulList = soup.find_all('ul', class_='list_con_li autoHeight')
    soup = BeautifulSoup(str(ulList[1]), 'lxml')
    a_labelList = soup.find_all('a')
    for item in a_labelList:
        chapter.append(item.get('title'))
        chapterLink.append(item.get('href'))
    return chapter, chapterLink


def main():
    chapter, chapterLink = getCatalogueAndLink(url)
    # verification
    with open('html.html', 'w') as file:
        for i in range(len(chapter)):
            file.write(str(chapter[i])+'  -->  '+str(chapterLink[i])+'\n')


if __name__ == '__main__':
    main()
