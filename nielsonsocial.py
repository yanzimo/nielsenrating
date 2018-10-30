import sys
from bs4 import BeautifulSoup
import urllib
import html
from HTMLParser import HTMLParser
import htmllib
import re
from lxml.html.clean import Cleaner
import pandas as pd

# the website is  : https://www.nielsensocial.com/socialcontentratings/weekly/

#the data format: rank, network,program,date

file = open('nielsonsocial.txt')
html_soup = BeautifulSoup(file, 'html.parser')

table_containers = html_soup.find_all('div', class_='table-container')


#extract first list, weekly top 10 series and specials and first rank
list_1 = table_containers[0]
list_1_rank = list_1.find('td',class_='rank first').text
list_1_network = list_1.find('span',class_='black-network').text
list_1_title = list_1.find('div',class_='program-name').text
list_1_date = list_1.find('div',class_='date').text
#interactions needs to be stripped
list_1_interactions = list_1.find('div',class_='interactions').text.strip()

tdata = [[list_1_rank,list_1_network, list_1_title,list_1_date,list_1_interactions]]

test_data = pd.DataFrame(tdata,columns=['Rank','Network','Title','Date','Interactions'])


#containers = []
rank = []
network = []
title= []
date = []
interactions = []



#total 3 lists, this is the first list, weekly top10, series and specials
chart = table_containers[0]

ranks = 11
a= 0
while a<ranks:
    rank_data = chart.find_all('tr')[a]

    tr_rank= rank_data.find_all('td',{'class':['rank first','rank ']})

    for tr_rank1 in tr_rank:
        rank_text = tr_rank1.text
        rank.append(rank_text)
                #print(rank)
            #tr_program= rank_data.find_all('td',{'class':'program'})
    tr_network = rank_data.find_all(lambda tag: tag.name == 'span' and tag.get('class')==['black-network'])
    for tr_network1 in tr_network:
            #print(tr_network1)
        network_text = tr_network1.text
        network.append(network_text)

    tr_title= rank_data.find_all('div',{'class':'program-name'})
    for tr_title1 in tr_title:
        #print(tr_title1)
        title_text = tr_title1.text
        title.append(title_text)

        #date only have 20, the third list does not have dates
    tr_date = rank_data.find_all('div',{'class':'date'})
    for tr_date1 in tr_date:
        date_text = tr_date1.text
        date.append(date_text)
            #print(date_text)


    tr_interactions = rank_data.find_all('div',{'class':'interactions'})
    for tr_interactions1 in tr_interactions:
        interaction_text = tr_interactions1.text.strip()
        interactions.append(interaction_text)
        #print(rank_data)
    a = a+1

    #print(chart)
#This is the second chart about sport events
s_chart = table_containers[1]
s_rank = []
s_network = []
s_title= []
s_date = []
s_interactions = []

s_ranks = 11
s_a= 0
while s_a<s_ranks:
    rank_data = s_chart.find_all('tr')[s_a]

    tr_rank= rank_data.find_all('td',{'class':['rank first','rank ']})

    for tr_rank1 in tr_rank:
        rank_text = tr_rank1.text
        s_rank.append(rank_text)
                #print(rank)
            #tr_program= rank_data.find_all('td',{'class':'program'})
    tr_network = rank_data.find_all(lambda tag: tag.name == 'span' and tag.get('class')==['black-network'])
    #print(tr_network)
    for tr_network1 in tr_network:
            #print(tr_network1)
        network_text = tr_network1.text
        s_network.append(network_text)

    tr_title= rank_data.find_all('span',{'class':'black-network extra-name'})
    for tr_title1 in tr_title:
        #print(tr_title1)
        title_text = tr_title1.text
        s_title.append(title_text)

        #date only have 20, the third list does not have dates
    tr_date = rank_data.find_all('div',{'class':'date'})
    for tr_date1 in tr_date:
        date_text = tr_date1.text
        s_date.append(date_text)
            #print(date_text)


    tr_interactions = rank_data.find_all('div',{'class':'interactions'})
    for tr_interactions1 in tr_interactions:
        interaction_text = tr_interactions1.text.strip()
        s_interactions.append(interaction_text)
        #print(rank_data)
    s_a = s_a+1


test_data_seriesandspecials= pd.DataFrame({'Rank':rank,'Network':network,'Title':title,'Date':date,'Interactions':interactions})

test_data_sports= pd.DataFrame({'Rank':s_rank,'Network':s_network,'Title':s_title,'Date':s_date,'Interactions':s_interactions})



#panda frame show the whole chart
pd.set_option('display.expand_frame_repr',False)
print(test_data_seriesandspecials)
print(test_data_sports)
#end = test_data_seriesandspecials.append(test_data_sports)
#print(end)

#to csv
test_data_seriesandspecials.to_csv('tv_rating_series.csv',encoding='utf-8',index=False)
test_data_sports.to_csv('tv_rating_sports.csv',encoding='utf-8',index=False)