from dpla.api import DPLA
#how to access your 'API_KEY' so you don't have to enter every time
#os lets you look at your computer
import os
#pull your API_KEY
my_api_key = '6fe82fec460e727f153f50b9e6b28e07'
#open a connection with the DPLA API.
dpla_connection = DPLA(my_api_key)

#use requests library
import requests

#add an endpoint where we can make requests
endpoint = 'https://api.dp.la/v2/items'
#set parameters to get information about Austi, Texas
params = {
'api_key': my_api_key,
'q': "Austin, Texas",
}
#let's get the requests back!
requested_the_hard_way = requests.get(endpoint, params)
requested_the_hard_way.status_code
#print the URL
print("****")
print(requested_the_hard_way.url)
#print the number of results
print("****")
print(requested_the_hard_way.json()['count'])
#print the 'docs'(?) for the first page of results
print("****")
print(requested_the_hard_way.json()['docs'][0])
print("****")
#let's use the math.ceil function so we can see how many pages we need to iterate over. we're going to go to 20 pages
import math
#define the total_hard_way_results as an empty list
total_hard_way_results = []
#set the parameters: enter your api key, the query, and the number of pages
params = {
    'api_key': my_api_key,
    'q': 'Austin, Texas',
    'page_size': '500'
}
#total results will equal the page count
total_results = requested_the_hard_way.json()['count']
#we use the math.ceil funtion to round up the number get to see how many pages we have
number_of_pages = math.ceil(total_results/500)
print(number_of_pages)
#we're going through the first 20 pages
list_of_page_numbers = range(1, 21, 1)
#for each page_number in list_of_page_numbers, print the page number of that page
for page_number in list_of_page_numbers:
    print(page_number)
    params['page'] = list_of_page_numbers
    #add these results to your list!
    for result in requests.get(endpoint, params).json()['docs']:
        total_hard_way_results.append(result)
#print the count of items in total_hard_way_results
print(len(total_hard_way_results))
print("****")
#create an empty dictionary called state_results
state_results = {}
state_results['other_format'] = 0
for item in total_hard_way_results:
    if 'stateLocatedIn' in item['sourceResource']:
        if item['sourceResource']['stateLocatedIn'][0]['name'] in state_results:
            state_results[item['sourceResource']['stateLocatedIn'][0]['name']] += 1
        else:
            state_results[item['sourceResource']['stateLocatedIn'][0]['name']] = 1
    elif 'format' in item['sourceResource'] and item['sourceResource']['format'] != 'Text':
        state_results['other_format'] += 1
    else:
        pass

print(state_results)
