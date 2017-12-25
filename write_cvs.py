import pandas as pd

class optinCsv():
    @staticmethod
    def write(list,csvName,map):
        try:
         df=pd.DataFrame(map,columns=list)
         df.to_csv(csvName,encoding='utf-8')
        except Exception as e:
            print(e)
    @staticmethod
    def read(csvName):
        df2=pd.read_csv(csvName,encoding='utf-8')
        return df2

