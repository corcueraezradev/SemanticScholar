# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:09:10 2024

@author: ezbox
"""

#define a custom header called x-api-key


import requests
from pprint import pprint

# Define the API endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/search'

# More specific query parameter
query = input("Search: ")
query_params = {'query': query, 'limit': 3}

# Directly define the API key (Reminder: Securely handle API keys in production environments)
api_key = 'LbTmvJOR4ej5gZT1iUzn20CeXstaPkaan86TOwPg'  # Replace with the actual API key

# Define headers with API key
headers = {'x-api-key': api_key}

# Send the API request
response = requests.get(url, params=query_params, headers=headers)

# Check response status
if response.status_code == 200:
   response_data = response.json()
   # Process and print the response data as needed
   pprint(response_data)
else:
   print(f"Request failed with status code {response.status_code}: {response.text}")