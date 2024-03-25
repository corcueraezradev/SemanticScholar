# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:42:38 2024

@author: ezbox
"""

import requests
from pprint import pprint
from environment import api_key
from datetime import datetime

# Define the paper search endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/search'

# query = input("Search: ")
query = 'covid'

# Define the required query parameter and its value (in this case, the keyword we want to search for)
query_params = {
    'offset':0,
    'query': query,
    'year': '2020-',
    'limit': 100,
    'fields': 'externalIds,citationCount,title'
}

# Define headers with API key
headers = {'x-api-key': api_key}

# Define a separate function to make a request to the paper details endpoint using a paper_id. This function will be used later on (after we call the paper search endpoint).
def get_paper_data(paper_id):
    url = 'https://api.semanticscholar.org/graph/v1/paper/' + paper_id
    
    # Define which details about the paper you would like to receive in the response
    paper_data_query_params = {'fields': 'title,year'}
    
    # Send the API request and store the response in a variable
    response = requests.get(url, params=paper_data_query_params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def call_next():
    print("Next")
    offset = query_params.get("offset") + 100
    query_params.update(offset=offset)
    
    nextSearchResponse = requests.get(url, params=query_params, headers=headers)
    if nextSearchResponse.status_code == 200:
        nextSearchResponse = nextSearchResponse.json()
        return nextSearchResponse
    else:
        # Handle potential errors or non-200 responses
        print(f"Relevance Search Request failed with status code {search_response.status_code}: {search_response.text}")
      
def find_paper():
    for paper in search_response['data']:
        print(paper['externalIds'].val())
        # for extId in paper['externalIds']:
            # print(extId.val())
            # if extId == 'DOI':
            #     if ext
        # if paper['externalIds'][1] == '10.1016/S0140-6736(20)30183-5':
            # print(paper['paperId'])

startTime = datetime.now()                  
print(startTime)
 
# Initial            
# Make the GET request to the paper search endpoint with the URL and query parameters
search_response = requests.get(url, params=query_params, headers=headers)

# Check if the request was successful (status code 200)
if search_response.status_code == 200:
    search_response = search_response.json()    
    
    if search_response["total"] >= 1000:
        for page in range(2):   # this will query 500 results
            # get next page        
            next_response = call_next()
            search_response["data"]= search_response["data"] + next_response["data"]
            
    countNoDOI = 0
    for paper in search_response['data']:
        # for extId in paper['externalIds']:
        # print(str(paper['externalIds'].get('DOI')) + ' citation-count: ' + str(paper['citationCount']) + paper['title'])
        if paper['externalIds'].get('DOI') == None:
            countNoDOI += 1
            print(paper['title'] + str(paper['externalIds'].get('CorpusId')))
            
    
    # pprint(search_response)
    print('No DOI: ' + str(countNoDOI))
    print("Finished querying") 
    endTime = datetime.now()
    print(endTime-startTime)
        
    # resItem = int(input("Enter item #: "))
    
    # # Retrieve the paper id corresponding to the result item NUMBER in the list
    # paper_id = search_response['data'][resItem]['paperId']
    
    # # Retrieve the paper details corresponding to this paper id using the function we defined earlier.
    # paper_details = get_paper_data(paper_id)
    
    # # Check if paper_details is not None before proceeding
    # if paper_details is not None:
      
    #   pprint(paper_details)
      
    # else:
    #   print("Failed to retrieve paper details.")

else:
  # Handle potential errors or non-200 responses
  print(f"Relevance Search Request failed with status code {search_response.status_code}: {search_response.text}")
  