import re
 
class Monitor:
 #远期合约 近期合约 正常差值（远期-近期） 偏高预警(工作) 偏低预警（了结）    
    DValue = ''

    def __init__(self,request,forward,recent,normalValue,highValue,lowValue):
        self.request = request
        self.forward = forward
        self.recent = recent
        self.normalValue_h = normalValue
        self.normalValue_l = normalValue
        self.highValue = highValue
        self.lowValue = lowValue
        

#执行监控动作 先去请求 get返回的信息 处理 赋值 数值预警
    def checking(self):
        self.responseStr = self.request.process([self.forward.code,self.recent.code])
        self.dealerReponse()
        
        
        
#处理数值计算
    def dealerReponse(self):
        matchObj = re.findall( r'"(.*)"', self.responseStr, re.M|re.I)
        forwardArr = matchObj[0].split(',')
        recentArr = matchObj[1].split(',')
        self.forward.price = forwardArr[8]
        self.recent.price = recentArr[8]
        self.DValue = (float)(self.forward.price)-(float)(self.recent.price)
        
        print("远期（"+self.forward.code+")价格："+self.forward.price)
        print("远期（"+self.recent.code+")价格："+self.recent.price)
        if(self.DValue<self.lowValue):
            print("偏低预警:买入"+self.forward.code+";卖出"+self.recent.code)
            
            
        if(self.DValue>self.highValue):
            print("步入正常差价买入"+self.recent.code+";卖出"+self.forward.code)
            

        
