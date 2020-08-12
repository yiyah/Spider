import requests
import os
import re
from bs4 import BeautifulSoup
import ffmpy3  # need to configure ffmpeg


def getSearchResult(movieName):
    request_headers = {
        'Host': 'www.jisudhw.com',
        'Origin': 'http://www.jisudhw.com',
        'Referer': 'https://blog.csdn.net/c406495762/article/details/106095607',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    request_queryStringParam = {
        'm': 'vod-search'
    }

    request_data = {
        'wd': movieName,
        'submit': 'search'
    }

    server = 'http://www.jisudhw.com/'
    html = requests.post(server, data=request_data, params=request_queryStringParam, headers=request_headers)
    html.encoding = 'utf-8'
    return html.text


def parseBody(html):
    video_name = []
    video_link = []

    soup = BeautifulSoup(html, 'lxml')
    search_spans = soup.find_all('span', class_='xing_vb4')
    
    for span in search_spans:
        video_name.append(span.text)
        video_link.append('http://www.jisudhw.com'+span.a.get('href'))
    
    return video_name[0], video_link[0]


def getVideoPicsLink(url):
    video_piece_num = 0  # 电影集数
    video_piece_links = []  # 电影每一集的链接，用列表保存
    video_piece_dic = {}  # 电影每一集的链接，用字典保存

    headers = {
        'Host': 'www.jisudhw.com',
        'Referer': 'http://www.jisudhw.com/index.php?m=vod-search',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    input_list = soup.find_all('input')
    for url in input_list:
        if 'm3u8' in url.get('value'):
            video_piece_num += 1
            video_piece_links.append(url.get('value'))
            video_piece_dic[url.get('value')] = video_piece_num
    
    return video_piece_links


def main():
    html = getSearchResult('鹿鼎记')
    video_name, video_link = parseBody(html)  # 默认返回第一个搜索结果
    video_piece_links = getVideoPicsLink(video_link)

    if os.path.exists(video_name):
        os.system("rm -r {}/".format(video_name))
    os.mkdir(video_name)

    num = 0
    for link in video_piece_links:
        num += 1
        ffmpy3.FFmpeg(inputs={link: None}, outputs={'%s/第%d集.mp4'%(video_name, num):None}).run()
    

if __name__ == "__main__":
    main()