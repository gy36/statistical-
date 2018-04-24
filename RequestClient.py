import urllib.request

class RequestClient:
    
    url   = ""
    
    def __init__(self,url):
        self.url = url
        
    def process(self,param):
        self.param = ",".join(param)
        req=urllib.request.Request(self.url+self.param)
        
        response=urllib.request.urlopen(req)

        self.responseStr = (str)(response.read().decode("GBK"))
        
        response.close()
        
        return self.responseStr
