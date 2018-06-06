#make sure you $ pip install DPLA on CLI first
#??
from dpla.api import DPLA
#how to access your 'API_KEY' so you don't have to enter every time
#os lets you look at your computer
import os
#pull your API_KEY
my_api_key = '6fe82fec460e727f153f50b9e6b28e07'
#open a connection with the DPLA API.
dpla_connection = DPLA(my_api_key)
#let's search for cats!
result = dpla_connection.search('austen')
print(type(result))
print("***")
#turns the results into a string and prints the first 1000 characters?
print(str(result.__dict__)[:1000])
print("***")
#let's view a specific item in that list
item = result.items[0]
print(item)
print("***")
#walking the data to the source resource, and then the heading we want to reach
print(item['sourceResource']['stateLocatedIn'])
print("***")
#prints the sourceResource content
print(result.items[0]['sourceResource'])
#prints the keys of the dictionary for us to review
print(item.keys())
#for each entry in results, print the soureResource:stateLocatedIn info. if it doesn't have stateLocatedIn, print format. 
for entry in result.items[:9]:
    if 'stateLocatedIn'in entry['sourceResource']:
        print(item['sourceResource']['stateLocatedIn'])
    else:
         print(item['sourceResource']['format'])
