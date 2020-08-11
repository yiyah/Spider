import requests
import re
from bs4 import BeautifulSoup


url = 'http://www.jisudhw.com/?m=vod-detail-id-62426.html'


def getVideoPicsLink(url):
    video_piece_links = []
    headers = {
        'Host': 'www.jisudhw.com',
        'Referer': 'http://www.jisudhw.com/index.php?m=vod-search',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    h3_list = soup.find_all('h3')
    # 应该找h3 的 parent 的 div 就可以包括链接的 ul
    if len(h3_list) > 1:
        for h3 in h3_list:
            for text in h3.span:
                if 'm3u8' in text.string:
                    video_piece_links = h3
                    break
    
    return video_piece_links

def main():
    video_piece_links = getVideoPicsLink(url)
    with open('html1.html', 'w') as f:
        f.write(str(video_piece_links))


if __name__ == '__main__':
    main()
