'''
    File name: data_extract.py
    Author: Daniel G Perico Sánchez
    Date created: 21/01/2019
    Date last modified: 23/01/2019
    Python Version: 3.7.2
'''

#Import the needed libraries
from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import re
from collections import OrderedDict

#Extract the HTML code from de url
url = 'https://www.datacamp.com/tracks/data-scientist-with-python'
r = requests.get(url)
text = r.text
soup = BeautifulSoup(text)

#Extract the links that appear on the page
a_tags = soup.find_all('a')
links = []
for link in a_tags:
    i = link.get('href')
    links.append(i)

#We're looking for the courses datasets.
#So we extract with a simple regular expression those elements who satisfy the expression
pattern = '(courses\/)(.{1,})'
matches_list = []
for i in range(0,len(links)):
    matches = re.findall(pattern,links[i])
    matches_list.append(matches)

#Create a new list to save the non empty elements from de matches_list
matches_list_fix = []
for i in range(0,len(matches_list)):
    if len(matches_list[i]) == 1:
        matches_list_fix.append(matches_list[i])
    else:
        pass

#Discard those duplicated elements
courses_duplicated = []
for i in range(0,len(matches_list_fix)):
    name = matches_list_fix[i][0][1]
    courses_duplicated.append(name)
courses = list(OrderedDict.fromkeys(courses_duplicated))

#Create a list to save just the link to the dataset
data_links = []
for i in range(0,len(courses)):
    course_url = 'https://www.datacamp.com/courses/' + courses[i]
    r = requests.get(course_url)
    text = r.text
    soup = BeautifulSoup(text)
    a_tags = soup.find_all('a', class_ = 'link-borderless')

    for link in a_tags:
        i = link.get('href')
        data_links.append(i)

#Create a regular expression to obtain just the csv files
pattern_2 = '((https:\/\/assets\.)([\w.\/-]+)csv)'
data_matches_list = []
for i in range(0,len(data_links)):
    matches = re.findall(pattern_2,data_links[i])
    data_matches_list.append(matches)

#Discard the empty elements from the matches list
data_matches_list_fix = []
for i in range(0,len(data_matches_list)):
    if len(data_matches_list[i]) == 1:
        data_matches_list_fix.append(data_matches_list[i])
    else:
        pass

#Obtain the just the link from the data_matches_list
data_links_csv = []       
for i in range(0,len(data_matches_list_fix)):
    data_url = data_matches_list_fix[i][0][0]
    data_links_csv.append(data_url)

#Create a regular expression to obtain the csv file names
save_file_pattern = '(\w{1,}\.csv)'
saving_matches_names = []
for i in range(0,len(data_links_csv)):
    saving_matches = re.findall(save_file_pattern,data_links_csv[i])
    saving_matches_names.append(saving_matches)

#Save the datasets locally
for i in range(0,len(data_links_csv)):
    url = data_links_csv[i]
    r = requests.get(url)
    print('Saving: '+ str(saving_matches_names[i][0]))
    urlretrieve(url,'test/'+ str(saving_matches_names[i][0]))
