import requests
from bs4 import BeautifulSoup


url = "https://unsplash.com/"


def main():
    html = requests.get(url)
    with open("html.html", "w") as f:
        f.write(html.text)


if __name__ == '__main__':
    main()