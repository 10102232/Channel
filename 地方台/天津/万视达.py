import uuid
import time
import datetime
from MD5 import get_token
t=str(int(time.time()))
u=uuid.uuid4()
a=get_token(message=t)
url='http://live1.wisetv.com.cn/TJIPTV/TJXW.m3u8?auth_key='+t+'-0-0-'+a+'&GUID='+str(u).replace('-','')
print(url)