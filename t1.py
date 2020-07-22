import json
import matplotlib.pyplot as plt
from datetime import datetime as d
%matplotlib inline

with open('data.json' , 'r') as currency:
  data = json.load(currency)


def T1():
  d_1 = d(2019,1,1)
  d_2 = d(2019,1,31) 
  sort = sorted(data['rates'])
  values = list()
  dates = list()


  for i in sort:
    strip_time_from_date = d.strptime(i,'%Y-%m-%d')
    if strip_time_from_date <= d_2 and strip_time_from_date >= d_1:
      values.append(data['rates'][i]['INR'])
      dates.append(strip_time_from_date.day)

  plt.plot(dates, values)
  plt.xlabel('January 2019')
  plt.ylabel('Value of INR and EUR')
  plt.title('INR exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019')
  plt.legend(['INR vs. EUR'],loc = 'lower right')
  plt.show()


T1()