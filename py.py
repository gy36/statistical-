import urllib.request
import re
import time
from Period import Period
from RequestClient import RequestClient
from Monitor import Monitor
import os
import winsound



winsound.PlaySound('p.mp3', flags=1)


forward = Period("I1807")
recent  = Period("I1809")

request = RequestClient("http://hq.sinajs.cn/list=")


# 正常值 了结价格 偏低值
monitor = Monitor(request,forward,recent,-20,-25,-30)

while True:
    time.sleep(1)
    monitor.checking()
print(monitor.DValue)
print(forward.price)
print(recent.price)
