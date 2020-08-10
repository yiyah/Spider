import requests
import re
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from contextlib import closing
import os
import time


mainPage = 'https://www.dmzj.com/info/yaoshenji.html'


def getCatalogueAndLink(url):
    chapters = []
    chapterLinks = []

    # step1: get html
    html = requests.get(url)

    # step2: parse
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.find_all('h1')[0].text
    ulList = soup.find_all('ul', class_='list_con_li autoHeight')
    soup = BeautifulSoup(str(ulList[1]), 'lxml')
    a_labelList = soup.find_all('a')
    for item in a_labelList:
        chapters.append(item.get('title'))
        chapterLinks.append(item.get('href'))
    return title, chapters, chapterLinks


def getImgURl(url):
    
    imgURLList = []

    # step1: get script
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    scripts = soup.find_all('script', type="text/javascript")
    imgNameList = re.findall(r'\d{13,14}', str(scripts[0]))

    # step2: sort the list
    imgNameList.sort()

    # step3 get somg info about the image url
    chapterpic_front = re.findall(r'\|(\d{4})\|', str(scripts[0]))[0]
    chapterpic_back = re.findall(r'\|(\d{5})\|', str(scripts[0]))[0]

    # step4: splising the url
    for imgName in imgNameList:
        imgURLList.append("https://images.dmzj.com/img/chapterpic/"+chapterpic_front+'/'+chapterpic_back+
            '/'+imgName+'.jpg')

    return imgURLList


def DownloadImg(url, path):
    # urlretrieve(url, path)  # need refer, so this method is unavailable
    download_header = {
        'Referer': 'https://www.dmzj.com/view/yaoshenji/41917.html'
    }
    with closing(requests.get(url, headers=download_header, stream=True)) as response:
        chunk_size = 1024
        content_size = int(response.headers['content-length'])  
        if response.status_code == 200:
            print('文件大小:%0.2f KB' % (content_size / chunk_size))
            with open(path, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):  
                    file.write(data)
        else:
            print('链接异常')


def main():
    title, chapters, chapterLinks = getCatalogueAndLink(mainPage)

    if os.path.exists(title):
        os.system("rm -r {}/".format(title))
    else:
        os.mkdir(title)
    
    for chapter, chapterLink in zip(chapters, chapterLinks):
        os.makedirs(title+'/'+chapter)
        img_count = 0
        imgURLList = getImgURl(chapterLink)
        for imgURL in imgURLList:
            img_count += 1
            DownloadImg(imgURL, '%s/%s/%d.jpg' % (title, chapter, img_count))
            time.sleep(5)  # slow
            

if __name__ == '__main__':
    main()