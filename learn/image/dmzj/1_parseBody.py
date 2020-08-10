import requests
import re
from bs4 import BeautifulSoup
from contextlib import closing

url = "https://www.dmzj.com/view/yaoshenji/76532.html"  # note that do not contain "#@page=x"
# want to get https://images.dmzj.com/img/chapterpic/3059/96396/15272970323531.jpg


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
    imgURLList = getImgURl(url)
    with open("html.html", 'w') as f:
        for i in range(len(imgURLList)):
            DownloadImg(str(imgURLList[i]), "%d.jpg" % (i+1))
            f.write(str(imgURLList[i])+'\n')


if __name__ == '__main__':
    main()
