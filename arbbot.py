import time, json,datetime
import requests
from flask import Flask
app=Flask(__name__)

@app.route('/' )
def start():
            # result={}
            # result['Bitstamp']=btstamp()
            # result['Bitfinex']=bitfinex()
            # result['Coinbase']=coinbase()
            # result['Kraken']=kraken()
            # filepath='/home/arpita/Arbbot/data.json'
            # with open(filepath,'w') as fp:
            #     json.dumps(result,fp)
            while(True):
    		  btstampUSDLive = float(btstamp())
    		  coinbUSDLive = float(coinbase())
    		  krakenUSDLive = float(kraken())
    		  bitfinexUSDLive = float(bitfinex())
    		#print"{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
    		  print ("Bitstamp Price in USD =", btstampUSDLive)
    		  print ("Bitfinex Price in USD =", bitfinexUSDLive)
    		  print ("Coinbase Price in USD =", coinbUSDLive)
    		  print ("Kraken Price in USD =", krakenUSDLive)
    		# print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            time.sleep(120)
            # return render_template("startTrading",result=result)


def btstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()['last'] 

def bitfinex(): 
    bitFinexTick = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    return bitFinexTick.json()['last_price']

def coinbase():
    coinBaseTick = requests.get('https://coinbase.com/api/v1/prices/buy') 
    return coinBaseTick.json()['amount']
def kraken():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker',data=json.dumps({"pair":"XXBTZUSD"}),
        headers={"content-type":"application/json"})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]

if __name__=="__main__":
    app.debug=True
    app.run()

