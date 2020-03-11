import requests
import rsa

class getCookie:
    def __init__(self,user,passwd):
        self.user=user
        self.passwd=passwd

    #读取access_key
    def get_access_key_kaaass(self) :
        post_data = {'user':self.user,'passwd':self.passwd}
        access_key_data = requests.post("https://api.kaaass.net/biliapi/user/login",post_data)
        if access_key_data.status_code == 200 :
            access_key_text = access_key_data.text
            key1 = access_key_text.find('access_key')
            access_key = access_key_text[key1+13 : access_key_text.find('"',key1+14)] #13也一样
            return access_key
        else :
                raise RuntimeError('Error:' + str(access_key_data.status_code))

    #读取cookie
    def get_cookie(self) :
        url_cookie = 'https://api.kaaass.net/biliapi/user/sso?access_key=' + self.get_access_key_kaaass()
        cookie_res = requests.get(url_cookie)
        if cookie_res.status_code == 200 :
            cookie_text = cookie_res.text
            key1 = cookie_text.find('cookie')  
            return cookie_text[key1+9 : cookie_text.find('"',key1+11)]
        else :
            raise RuntimeError('Error:failed to get cookie,' + str(cookie_res.status_code))


if __name__ == '__main__' :
    print (getCookie('sakura-wrx@outlook.com','sakura-wrx').get_cookie())