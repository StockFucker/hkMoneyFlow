import pandas as pd
import urllib.request
import urllib.error
import json
import datetime

def getUrl():
    url = 'http://proxy.finance.qq.com/ifzqgtimg/appstock/app/dapan/index'
    data = urllib.request.Request(url)
    try:
        data = urllib.request.urlopen(data)
        result = json.loads(data.read().decode('utf-8'))
        result = result["data"]
        zjlx = result['zjlx']
        zjlx = [tick.split(" ") for tick in zjlx]
        df = pd.DataFrame(zjlx)
        df.columns = ["minute","sh","sz"]
        df = df.set_index(["minute"])
        datetime_str = datetime.datetime.now().strftime("%Y%m%d")
        df.to_csv("data/" + datetime_str + ".csv")
    except urllib.error.URLError as e:
        print (e.read().decode('utf-8'))



if __name__ == "__main__":
    getUrl()
