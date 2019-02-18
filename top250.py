##电影影评Top250推荐
import requests
import urllib
import time
import json
import sys
import re

def getMovieID(url):
    mov_id=[]
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    rq=urllib.request.Request(url)
    page=urllib.request.urlopen(rq)
    page=page.read().decode().translate(non_bmp_map)

    mems=re.findall(r'https://movie.douban.com/subject/\d*/',page)
    for mem in mems:
        ls=re.split('/',mem)[4]
        mov_id.append(ls)
        print(ls)

    mov_id=set(mov_id)

    return mov_id

def getTopMovie250():
    movids=[]
    for num in range(0,5):
        s=getMovieID(url='https://movie.douban.com/top250?start=%d'%num*25)
        print(s)
        movids.extend(s)
        time.sleep(2)

    print("\n\n\n\n\n\nsorted",movids,"\n电影数量",str(len(movids)))
    return movids

def getMovData():
    movids=getTopMovie250()
    for movid in movids:
        url="https://api.douban.com/v2/movie/"+movid
        r=requests.get(url)
        print(r.status_code)
        r=r.json()
        write_down_json(r)
        time.sleep(10)


def write_down_json(data):
    filename="movie_data\%s.json"%data['title']
    with open(filename,'a') as f:  
            f.write(json.dumps(data))








    
getMovData()
