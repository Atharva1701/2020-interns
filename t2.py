import json
import matplotlib.pyplot as plt
from datetime import datetime as d
%matplotlib inline

with open('data.json' , 'r') as currency:
  data = json.load(currency)



def T2():
  d_1 = d(2019,1,1)
  d_2 = d(2019,1,31)

  
  sort_data = sorted(data['rates'])

  inr = list()
  gbp = list()
  dates = list()

  for i in sort_data:
    date = d.strptime(i,'%Y-%m-%d')
    if date <= d_2 and date >= d_1:
      inr.append(data['rates'][i]['INR'])
      gbp.append(data['rates'][i]['GBP'])
      dates.append([date.day])


  plt.plot(dates,gbp)
  plt.plot(dates,inr)
  plt.title('INR and GBP exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019')
  plt.legend(['INR','GBP'],loc='center right')
  plt.show()


T2()
