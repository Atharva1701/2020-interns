import json
import matplotlib.pyplot as plt
from datetime import datetime as d
import requests
%matplotlib inline


def T4():
	resp = requests.get('https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-01-31')
	if resp.status_code != 200:
    		raise ApiError('GET  {}'.format(resp.status_code))


	data = resp.json()

	rate = sorted(data['rates'])

	inr = list()
	gbp = list()

	dates = list()

	for i in rate:
 	 strip_time = d.strptime(i,'%Y-%m-%d')
  	 inr.append(data['rates'][i]['INR'])
  	 gbp.append(data['rates'][i]['GBP'])
  	 dates.append([strip_time.day])


	plt.plot(dates,inr)
	plt.plot(dates,gbp)
	plt.xlabel('January 2019')
	plt.legend(["INR","GBP"],loc ='center right')
	plt.show()

T4()