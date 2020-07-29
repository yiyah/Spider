import requests


url = "http://www.biqukan.com/1_1094/5403177.html"


def main():
    html = requests.get(url)
    print(html.text)


if __name__ == '__main__':
    main()
