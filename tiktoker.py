import requests
import json
import time
import random
import os
import string
from multiprocessing import Pool
from datetime import datetime  
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="USERNAME",
  password="PASSWORD",
  database="tiktok3r2"
)
def clearme():
    zl="clear"
    os.system(zl)
################### FOR INSERT
z="0"
t="tiktok"
a=""
px="100"
symL0vArray = []
###################
session = requests.session()
def h3d3r(p,ps):
    clearme()
    print(f"""\x1b[30;38;5;70m RANDOM TIKTOKER \x1b[30;38;5;68m
 _______  ___   ___   _  _______  _______  ___   _  _______  ______   
|       ||   | |   | | ||       ||       ||   | | ||       ||    _ |  
|_     _||   | |   |_| ||_     _||   _   ||   |_| ||    ___||   | ||  
  |   |  |   | |      _|  |   |  |  | |  ||      _||   |___ |   |_||_ 
  |   |  |   | |     |_   |   |  |  |_|  ||     |_ |    ___||    __  |
  |   |  |   | |    _  |  |   |  |       ||    _  ||   |___ |   |  | |
  |___|  |___| |___| |_|  |___|  |_______||___| |_||_______||___|  |_|
                    To \x1b[1;38;5;137mMySQL - \x1b[1;38;5;147mPHPMYADMIN

\x1b[1;38;5;197m[ + ]\x1b[0m\x1b[1;38;5;117m Speed Processes \x1b[1;38;5;137m[ {p} ]
\x1b[1;38;5;197m[ + ]\x1b[0m\x1b[1;38;5;117m Loops \x1b[1;38;5;137m[ {ps} ]
""")
def timeisnow():
    today = datetime.today()
    timeisnow = today.strftime("%d/%m/%Y %H:%M%p")
    return(timeisnow)
linkShopTikApp = "https://shoptik-app.herokuapp.com:443/tikapi/videosV2"
def reqx(rs):
    symL0vArray = [2, 3, 4, 5]
    RanNum = random.choice(symL0vArray)
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_."
    pw_length = RanNum
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]
    wefdef1 = ''.join((random.choice('qwertyuioplkjhgfdsazxcvbnm') for i in range(1)))
    randomUsername = wefdef1+mypw
    hdr = {"Accept": "*/*", "Content-Type": "application/json", "Origin": "https://inspiring-easley-425fb2.netlify.app", "User-Agent": "StatsApp/3 CFNetwork/1331.0.7 Darwin/21.4.0", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    jsda={"username": f"{randomUsername}"}
    time.sleep(1)
    ss=session.post(linkShopTikApp, headers=hdr, json=jsda)
    readoutputjson = ss.json()
    isStatusOk = readoutputjson['status']
    po = ss.content
    if b"200" in po:
        vid_id = readoutputjson['data']['videos']
        if vid_id:
            for p in vid_id:
                file = open(f"output/{randomUsername}.json", "a+")
                file.write(f"{readoutputjson}\n")
                file.close()
                comments = p["comments"]
                cover = p["cover"]
                likes = p["likes"]
                shares = p["shares"]
                vid_id = p["vid_id"]
                views = p["views"]
                cover = '"'+str(cover)+'"'
                uid = ''.join([random.choice(string.digits) for n in range(10)])
                mycursor = mydb.cursor()
                sql = f"INSERT INTO `tiktoker`(`uid`, `time`, `hide`, `delete`, `addedby`, `type`, `name`, `comments`, `cover`, `likes`, `shares`, `vid_id`, `views`) VALUES ('{uid}','{timeisnow()}','{z}','{z}','{a}','{t}','{randomUsername}','{comments}','{cover}','{likes}','{shares}','{vid_id}','{views}')"
                mycursor.execute(sql)
                mydb.commit()               
        else:
            uid = ''.join([random.choice(string.digits) for n in range(10)])
            mycursor = mydb.cursor()
            sql = f"INSERT INTO `tiktoker`(`uid`, `time`, `hide`, `delete`, `addedby`, `type`, `name`, `comments`, `cover`, `likes`, `shares`, `vid_id`, `views`) VALUES ('{uid}','{timeisnow()}','{z}','{z}','{a}','{t}','{randomUsername}','','','','','','')"
            mycursor.execute(sql)
            mydb.commit()                
        print(f"\x1b[1;38;5;119m[ ✔ ]\x1b[0m\x1b[1;38;5;119m  {isStatusOk}\x1b[0m Found : \x1b[1;38;5;119m{randomUsername} -> /output/RANDOM-{randomUsername}.json\x1b[0m")
    else:
        #print(f"\x1b[1;38;5;197m[ x ]\x1b[0m \x1b[1;38;5;197m {isStatusOk}\x1b[0m \x1b[1;38;5;244mno username found :\x1b[1;38;5;197m {randomUsername} \x1b[0m")
        pass
    symL0vArray.append(RanNum)
h3d3r(10,1000)
ps=input("How many loop (default 1000) :") or 1000
ps=int(ps)
h3d3r(10,ps)
p=input("How many process(default 10) :") or 10
p=int(p)
h3d3r(p,ps)
possibleCharXXX = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
RanUsernameXXX = ''.join(random.choice(possibleCharXXX) for i in range(ps))
with Pool(processes=p) as pool:  
    print(pool.map(reqx, RanUsernameXXX))
