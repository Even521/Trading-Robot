import  time
#
#高频交易
#
from zb_api_data import zb_api_data


class zb_api_high_trade(object):
    @staticmethod
    def get_deth_list(currency,size):
        api=zb_api_data(currency)
        dict= api.depth(size)
        map={"time":zb_api_high_trade.time_format(dict['timestamp'])}
        if dict is not None:
           sell=float(zb_api_high_trade.list_sum_number(dict['asks']))
           buy= float(zb_api_high_trade.list_sum_number(dict['bids']))
           if(sell-buy<0):
             print("买入量大于卖出量")
             print(dict['bids'][size-1])
             price=int(dict['bids'][size-1][0])
             last=price+0.02
             print(last)
           else:
               print(dict['bids'])
               print(dict['asks'])

               print("买入量小于卖出量")

        return map
    @staticmethod
    def time_format(date):
        t=float(int(date)/1000)
        return time.strftime('%H:%M:%S', time.localtime(t))

    #求和
    @staticmethod
    def list_sum_number(list):
        num = 0
        for i in list:
         num += i[1]
        return num
    @staticmethod

    def start(c,s):
       while(True):
        zb_api_high_trade.get_deth_list(c,s)
        time.sleep(1)


if __name__ == '__main__':
    zb_api_high_trade.start('bts_btc',10)


