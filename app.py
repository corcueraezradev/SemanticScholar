# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:19:40 2024

@author: machine
"""

import streamlit as st
# import os
import requests
# from pprint import pprint
from environment import api_key
   
url = 'https://api.semanticscholar.org/graph/v1/paper/search'

# Define headers with API key
headers = {'x-api-key': api_key}

st.title("SmartResearch")
st.markdown("The research paper search engine platform")
query = st.text_input("Search:", placeholder = "Type here ...", key = "query") 

query_params = {
    'offset':0,
    'query': query,
    'year': '2020-',
    'limit': 50,
    'fields': 'title,year,abstract,authors.name,url,journal,externalIds,s2FieldsOfStudy,publicationTypes,publicationDate,referenceCount,citationCount,influentialCitationCount'
}

if st.button('Submit', key = "query_button") and query!='':
    
    # Initial            
    # Make the GET request to the paper search endpoint with the URL and query parameters
    search_response = requests.get(url, params=query_params, headers=headers)

    # Check if the request was successful (status code 200)
    if search_response.status_code == 200:
        search_response = search_response.json()    
        
        # if search_response["total"] >= 1000:
        #     for page in range(2):   # this will query 500 results
        #         # get next page        
        #         next_response = call_next()
        #         search_response["data"]= search_response["data"] + next_response["data"]

        
        # pprint(search_response)
        for paper in search_response["data"]:
            authorsList = ""
            for author in paper["authors"]:  
                authorsList = authorsList + author["name"] + ", "
                
            st.write("---")  
            st.markdown(paper["title"])  
            # st.caption(authorsList) 
            # st.caption("DOI:" + paper["externalIds"]["DOI"])
            # st.caption(paper["year"])
            st.caption("Citation Count: " + str(paper["citationCount"]))
            st.caption("Influential Citation Count" + str(paper["influentialCitationCount"]))
            # st.caption(paper["referenceCount"]+paper["citationCount"]+paper["influentialCitationCount"])
            st.caption("SmartScore: " + str(paper["citationCount"]+paper["influentialCitationCount"]))
            # st.caption(paper["url"])
                          
                
             
            
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
      
      text = "Relevance Search Request failed with status code" + search_response.status_code + ": " + search_response.text
      st.error(text)
    
    
    

# Verify OTP
if 'key' in st.session_state: 
    verify_otp = st.text_input("Verify OTP: ", placeholder = "Type here ...", key="verify_otp")

    if st.button('Verify', key = "verify_otp_button"):
        if verify_otp == st.session_state.key:
            st.success("OTP verified, you can login now")        
        else:
            st.error("Please check your OTP again")
