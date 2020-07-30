import requests


url = "https://www.biqukan.com/38_38836/497783246.html"
# url = "http://www.biqukan.com/1_1094/5403177.html"


def main():
    html = requests.get(url)

    # if use print, the content will damage.
    # so write the content in file.
    with open("html1.html", 'w') as f:
        f.write(html.text)


if __name__ == '__main__':
    main()
