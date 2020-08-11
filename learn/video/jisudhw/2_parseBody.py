import requests
from bs4 import BeautifulSoup

# 走个过程，就不处理的很完整了, 有名字和链接就行了


def getSearchResult(movieName):
    request_headers = {
        'Host': 'www.jisudhw.com',
        'Origin': 'http://www.jisudhw.com',
        'Referer': 'http://www.jisudhw.com/',
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
    
    return video_name, video_link


def main():
    html = getSearchResult("鹿鼎记")
    video_name, video_link = parseBody(html)
    with open('html1.html', 'w') as f:
        for (name, link) in zip(video_name, video_link):
            f.write(name+' --> ' +link+'\n')


if __name__ == '__main__':
    main()
