'''
    File name: data_extract.py
    Author: Daniel G Perico Sánchez
    Date created: 29/03/2019
    Date last modified: 29/03/2019
    Python Version: 3.7.2
'''

#!/usr/bin/env python
# coding: utf-8

#Import useful libraries
import requests
from urllib.request import urlretrieve

#Declare global variables to control query dates
years = [i for i in range(1970,2019)]
month = [1,2,3,4,5,6,7,8,9,10,11,12]
day = [1,31]
month_init_counter = 0
month_end_counter = 1

def extract():
    '''
    This funtion does not recieve any parameters
    Uses the USGS's API to extract earthquakes data around the world based on a date range
    The API has a 20000 events search limit so it goes in a independent query for every month or a range of years
    '''
    for j in range(len(month)):
        try:
            start_time = str(years[i])+'-'+str(month[j])+'-'+str(day[0])
            end_time = str(years[i])+'-'+str(month[j])+'-'+str(day[1])
            url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime='+start_time+'&endtime='+end_time
            urlretrieve(url,'data/data_'+start_time+'_'+end_time)
            print('Saving data_'+str(start_time)+'_'+str(end_time)+' in data/...')
        except:             
            pass

#For every year in the years list calls the extract function
for i in range(len(years)):
    extract()
