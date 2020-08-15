import requests
import base64
import json


AK = "your's AK"
AS = "your's AS"

def BeautifyImage(image_base64, whitening, smoothing):
    """
    whitening: range 0 to 100
    smoothing: range 0 to 100
    """
    data = {
        'api_key' : AK,
        'api_secret' : AS,
        'image_base64' : image_base64,
        'whitening' : whitening,
        'smoothing' : smoothing,
    }

    beautify_url = 'https://api-cn.faceplusplus.com/facepp/v1/beautify'
    res = requests.post(url=beautify_url, data=data)
    with open('html.html', 'w') as f:
        f.write(res.text)
    res_json = json.loads(res.text)
    return res_json


def main():
    img_path = 'test.jpg'
    with open(img_path, 'rb') as f:
        img_base64 = base64.b64encode(f.read())

    res_json = BeautifyImage(img_base64, 100, 100)

    base64_data = res_json['result']
    img_data = base64.b64decode(base64_data)
    with open("beautiful.jpg", 'wb') as f:
        f.write(img_data)
    pass


if __name__ == "__main__":
    main()