from requestget import geturl
from requestget import posturl
from MD5 import get_token
import requests
import time
import uuid
import hashlib
import re
import os
from DPL频道列表模板 import lists

'''
s=>>> s = "string"
>>> l = list(s)
>>> l.sort()
>>> s = "".join(l)
'''

ch={'小八':['64609','1561172967437','52957b3260db60e236d311d26476669e'],'YYF':['9999','1561173032405','305b1d4a03ab2b4010f51dba0c0fdae4'],'zsmj':['52876','1561173053039','09181f4d29a8b35a8b80d1e2fb1bd227'],'老陈':['74960','1561173293186','83b1213eef89b6802190d53abc120d17'],'Zard':['60937','1561173329281','a84cec993dd5c44cc26ddc1b0d8e75fc'],'imbatv':['19002','1561173376466','acfb27b7cc5af182fbe1782e3239a228'],'亚瑟':['59889','1561173473440','501a1054ca97a58b6afebfea9a3dc745'],'漫威':['1543154','1561173883640','dc30ef9952513a664cc75007ccbd3675'],'林正英':['218859','1561173957203','3f69d44026cb5a26e8d3c122cc913ddd'],'杰出':['3258','1561180106070','9d3ecca3793086c6cf7b853190e9502e'],'K9':['235520','1561200486299','a216b51bfa7ad42913622413c08a7909'],'820邹倚天':['507882','1561200533578','e320f31614dd5ad710096b4c037072e5'],'Zippo宝哥':['67554','1561200588328','b83fc31aa867f1f35d3e2397f125ebc0'],'跳刀':['237974','1561200638620','1bc0ab60794244095095f3bc5e74e1b3'],'baby半仙':['6599622','1561200692252','c603b88eae77eb31f2c6497096455d0d'],'Cty':['97389','1561200765193','1a401627512e69add77c385683875af3'],'lilith':['1972046','1561200798874','df1f3af970df1787e01cd2e74f90f5e1'],'烈女':['564867','1561200833909','03a2612548ca5c4eabd61689b1773728'],'':['','',''],'':['','',''],'':['','',''],'':['','',''],'':['','',''],'':['','',''],'':['','',''],'':['','',''],'':['','','']}
#预览
playurls=[]
rd=list(ch.keys())
rds=[]
for a,b in ch.items():
    h = {'Accept': 'application/json, text/plain, */*', 'auth':b[2],
         'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.douyu.com',
         'Referer': 'https://www.douyu.com/g_DOTA2', 'rid':b[0], 'time': b[1],
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    u='https://playweb.douyucdn.cn/lapi/live/hlsH5Preview/'+b[0]
    params ={'rid':b[0],'did':'f558a0158e7b70198133928d00041501'}
    r=requests.post(u,data=params,headers=h)
    r.encoding = 'utf-8'
    r = r.text
    #print(a,r)
    key=re.findall(r'live":"(.+?)_',r)
    if key==[]:
        #print(a,r)
        continue
    else:
        key=key[0]
        playurl='http://tx2play1.douyucdn.cn/live/'+key+'_8000p.flv'
        playurls.append(playurl)
        rds.append(a)
        print(a,playurl)
        #print('\n'+r+"\n")
with open('斗鱼.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('斗鱼.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(rds[j],u)
    with open('斗鱼.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\Channel\\斗鱼直播\\斗鱼.dpl')

'''
def __init__(self):
    self.baseUrl = "http://www.douyutv.com/api/v1/"
    self.midReq = "?aid=android&cdn=ws&client_sys=android&time="

def GetStringMD5(self, str):
    m = md5hash.new()
    m.update(str)
    return m.hexdigest()
def request(self, action, param=None):
    t = str(int(time.time()))
    md5_url = action + self.midReq + t + "1231"
    auth = self.GetStringMD5(md5_url)
    return auth
'''