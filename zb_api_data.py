import yaml
from request_call import request_call
#
#行情类

# with open("./application.yaml") as f:
#      resource=yaml.load(f)

class zb_api_data(request_call):

    def __init__(self,currency):
        self.host=request_call().resource['zb']['api']['url']
        self.currency=currency

    #参数字典
    def dict(self):
        dict={'market':self.currency}
        return dict

    #市场行情
    def ticker(self):
        url=self.host+"/data/v1/ticker"
        return request_call.zb_call(url,self.dict())
    #市场深度
    def depth(self,size):
        url=self.host+"/data/v1/depth"
        map=self.dict()
        map['size']=str(size)

        return request_call.zb_call(url,map)
    #历史成交
    def  trades(self):
        url=self.host+'/data/v1/trades'
        return request_call.zb_call(url,self.dict())
    #K线
    def kline(self):
        url=self.host+"/data/v1/kline"
        return request_call.zb_call(url,self.dict())


if __name__ == '__main__':
    a =zb_api_data('btc_usdt')
    print(a.ticker())