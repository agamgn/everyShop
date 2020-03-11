import requests

header={
    "Origin":"https://www.bilibili.com",
    "Referer": "https://www.bilibili.com/video/av95112103",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

data={
    "aid": 95112103,
    "like": 1,
    "csrf": "c2f19427ff8e8f7e10912a639d1a1838"
}
class Like:
    def __init__(self):
        self.likeUrl="https://api.bilibili.com/x/web-interface/archive/like"
    

    def getLike(self):
        html=requests.post(self.likeUrl,data,header).text
        print(html)