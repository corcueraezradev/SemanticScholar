# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:42:38 2024

@author: ezbox
"""

import requests
from pprint import pprint
from environment import api_key

# Define the paper search endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/search'

query = input("Search: ")

# Define the required query parameter and its value (in this case, the keyword we want to search for)
query_params = {
    'offset':0,
    'query': query,
    'limit': 100,
    'fields': 'title,year,abstract,authors.name,url,externalIds,s2FieldsOfStudy,publicationTypes,publicationDate'
}

# Define headers with API key
headers = {'x-api-key': api_key}

# Define a separate function to make a request to the paper details endpoint using a paper_id. This function will be used later on (after we call the paper search endpoint).
def get_paper_data(paper_id):
    url = 'https://api.semanticscholar.org/graph/v1/paper/' + paper_id
    
    # Define which details about the paper you would like to receive in the response
    paper_data_query_params = {'fields': 'title,year,abstract,authors.name'}
    
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
      
  
            
# Initial            
# Make the GET request to the paper search endpoint with the URL and query parameters
search_response = requests.get(url, params=query_params, headers=headers)

# Check if the request was successful (status code 200)
if search_response.status_code == 200:
    search_response = search_response.json()    
    
    if search_response["total"] >= 1000:
        for page in range(4):   # this will query 500 results
            # get next page        
            next_response = call_next()
            search_response["data"]= search_response["data"] + next_response["data"]
            
   

    
    pprint(search_response)
    print("Finished querying")    
        
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
  