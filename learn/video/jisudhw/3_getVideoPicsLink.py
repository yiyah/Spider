import requests
import re
from bs4 import BeautifulSoup


url = 'http://www.jisudhw.com/?m=vod-detail-id-62426.html'


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
    video_piece_links = getVideoPicsLink(url)
    print(len(video_piece_links))
    with open('html1.html', 'w') as f:
        f.write(str(video_piece_links))


if __name__ == '__main__':
    main()
