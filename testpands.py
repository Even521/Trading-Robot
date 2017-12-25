import pandas as pd

from zb_api_trade import zb_api_trade

a=zb_api_trade()

head=['enName','freez','unitDecimal','cnName','isCanRecharge','unitTag','isCanWithdraw','available','key']
l=a.get_account_info()
print(type(l))
t=l['result']['coins']
print(t)
df=pd.DataFrame(t,columns=head)
df.to_csv("test.csv",encoding='utf-8')
df2=pd.read_csv("test.csv",encoding='utf-8')
print(df2)
