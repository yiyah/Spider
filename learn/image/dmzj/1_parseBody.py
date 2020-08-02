import requests
from bs4 import BeautifulSoup


url = "https://www.dmzj.com/view/yaoshenji/76532.html"  # note that do not contain "#@page=x"


def main():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    script = soup.script
    print(script)
    # img_div = soup.find_all("div", class_="comic_wraCon autoHeight")
    # soup = BeautifulSoup(str(img_div[0]), 'lxml')
    # print(str(img_div[0].string))
    # img_url = soup.find_all('img')
    # img_url = img_url.get("src")
    # with open("html.html", 'w') as f:
        # f.write(html.text)


if __name__ == '__main__':
    main()
