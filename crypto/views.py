from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json
import time
def index(request):
    ethValues = []
    spd = 60*60*24
    url = "https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=USD&limit=168&aggregate=1&e=CCCAGG"
    myResponse = requests.get(url, verify=True)
    if(myResponse.ok):
        jData = json.loads(str(myResponse.content)[2:-1])["Data"]
        for i in range(90):
            ethValue = 0
            ethValue = jData[i]["close"]
            ethValues.append(ethValue)

    sentiment = 0.610913
    predictedValue = 5393.6*sentiment - 2957.3
    if predictedValue > ethValues[len(ethValues)-1]:
        prediction = 1
    else:
        prediction = 0
    c = {
        'ethValues': ethValues,
        'prediction': prediction,
        'predictedValue': int(predictedValue),
        'currentValue': int(ethValues[len(ethValues)-1])
    }
    return HttpResponse(loader.get_template('crypto/index.html').render(c))
