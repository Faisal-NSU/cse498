import time
import datetime
from keep_alive import keep_alive
import pandas as pd
from googletrans import Translator

#using this to make a host server
keep_alive()

#uploaded a splitted part of train.csv 
df = pd.read_csv('work.csv')

for i in range(10):
  translator = Translator(raise_exception=True)
  eng_list = df['Description'] 
  s = i * 100
  e = (i+1) *100
  eng_list = list(eng_list[s:e])
  newt = translator.translate(eng_list, dest='bn')
  
  bangla_list = []
  for t in newt:
    bangla_list.append(t.text)

  some = {'description': bangla_list}  
       
  last = pd.DataFrame(some) 
    
  # saving the dataframe 
  name = str(1100 + (i)*100)
  last.to_csv(name+'.csv',index=False)  
  print('gonna sleep ',i)
  now = datetime.datetime.now()
  print (now.strftime("%Y-%m-%d %H:%M:%S"))
  time.sleep(4500)
