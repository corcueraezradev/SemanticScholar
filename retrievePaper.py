# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:21:57 2024

@author: ezbox
"""

import requests
from pprint import pprint

# Define the paper search endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/search'

query = input("Search: ")


# Define the required query parameter and its value (in this case, the keyword we want to search for)
query_params = {
    'query': query,
    'limit': 100
}

# Directly define the API key (Reminder: Securely handle API keys in production environments)
api_key = 'LbTmvJOR4ej5gZT1iUzn20CeXstaPkaan86TOwPg'  # Replace with the actual API key

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

# Make the GET request to the paper search endpoint with the URL and query parameters
search_response = requests.get(url, params=query_params, headers=headers)

# Check if the request was successful (status code 200)
if search_response.status_code == 200:
  search_response = search_response.json()
  pprint(search_response)
  
  resItem = int(input("Enter item #: "))

  # Retrieve the paper id corresponding to the result item NUMBER in the list
  paper_id = search_response['data'][resItem]['paperId']

  # Retrieve the paper details corresponding to this paper id using the function we defined earlier.
  paper_details = get_paper_data(paper_id)

  # Check if paper_details is not None before proceeding
  if paper_details is not None:
    
    pprint(paper_details)
    
  else:
    print("Failed to retrieve paper details.")

else:
  # Handle potential errors or non-200 responses
  print(f"Relevance Search Request failed with status code {search_response.status_code}: {search_response.text}")