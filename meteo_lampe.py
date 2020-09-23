import requests
import json
import time
from datetime import datetime

def change_color(color):
  print "change color to " + color
  r = requests.get("https://changecolor-candle.glitch.me/" + color)



url = 'http://api.openweathermap.org/data/2.5/weather?q=Paris&appid=96b99a4ac05013d0b00f353b6e48a988&units=metric'
while 1: 

  r = requests.get(url)
  dict_obj = json.loads(r.text)
  print dict_obj
  temp =  dict_obj['main']['temp']
  print "temperature : " + str(temp)

  print datetime.now()
  if temp > 18:
    change_color('rouge')
  else:
    change_color('bleu')
  time.sleep(5)
