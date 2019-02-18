import requests
import webbrowser as wb
import json
import time

def Tuling():
    key='1163e827d44f40ba9fcba62fa5db2e85'
    api='http://www.tuling123.com/openapi/api?key='+key+'&info='
    
    if Test(api):
        Chatting(api)
        print("--欢迎您的使用--")

    
def Test(api=''):
    r=requests.get(api)
    k=str(r.status_code)
    if k=='200':
        print("\n----图灵机器人连接成功----")
        return 1
    else:
        print("\n重新连接中",end='')
        for i in range(3):
            print('.',end='')
            time.sleep(1)
        Tuling()
    


def Chatting(api):
    while True:
        words=input("我：")
        if words=='重启':
            Tuling()
        elif words=='结束':
            return 0
        api+=words
        back=requests.get(api)
        back=back.json()

        try:
            print("@robot:",back['text'])
            if back['url']:
                wb.open(back['url'],new=1,autoraise=True)
        except:
            pass
        
        




Tuling()
