import requests



def parseBody(movieName):
    request_headers = {
        'Host': 'www.jisudhw.com',
        'Proxy-Connection': 'keep-alive',
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


def main():
    html = parseBody("唐璜小姐")
    with open('html.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()