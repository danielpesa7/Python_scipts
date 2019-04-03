'''
    File name: data_extract.py
    Author: Daniel G Perico Sánchez
    Date created: 31/03/2019
    Date last modified: 02/04/2019
    Python Version: 3.7.2
'''

import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as beso
import re
import sys, os

country = str(sys.argv[2])
city = str(sys.argv[1])
year = [i for i in range(1970,2020)]

for k in range(len(year)):
    url = 'https://www.timeanddate.com/moon/phases/'+country+'/'+city+'?year='+str(year[k])
    page = rq.get(url)
    soup = beso(page.content,'html.parser')

    td = soup.find_all('tr')
    td_list = list(td)
    expression = r'(\w+\s\w+\s\w+\s\w+,\s\d+\s\w+\s\d+,\s\d+:\d+)'

    dates_list = []
    for i in range(len(td_list)):
        a_string = str(td_list[i])
        dates_expression = re.findall(expression,a_string)
        dates_list.append(dates_expression)

    final_list = []
    for i in range(len(dates_list)):
        if len(dates_list[i]) != 0:
            for j in range(len(dates_list[i])):
                a = dates_list[i][j]
                final_list.append(a)

    final_list_2= []
    for i in range(len(final_list)):
        final_list_2.append(final_list[i].split(','))

    data_df = pd.DataFrame(final_list_2, columns = ['Phase','Date','Time'])
    print('Saving_'+city+'_'+country+'_'+str(year[k])+'.csv')
    path = 'moon_data/'+country+'/'+city
    try:  
        os.makedirs(path)
    except OSError:  
        pass
    else:  
        print ("Successfully created the directory %s" % path)
        
    data_df.to_csv('moon_data/'+country+'/'+city+'/'+city+'_'+country+'_'+str(year[k])+'.csv')
