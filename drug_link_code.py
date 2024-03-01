#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Importing necessary libraries
import requests
import json

#Defining the class to make API calls
class MakeApiCall:
    def get_data(self, api):
        response = requests.get(api)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:# Catching and handling any HTTP errors
            print(f"Error: {e}")
            return
        # Printing a success message and parsing the response as JSON data 
        print("Successfully fetched the data")
        data = response.json()
        # Saving the JSON data to file
        self.save_data_to_file(data, "druglink3.json")

    def get_user_data(self, api, parameters):
        response = requests.get(api, params=parameters)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")
            return
        
        print("Successfully fetched the data with parameters provided")
        data = response.json()
        self.save_data_to_file(data, "druglink3_filtered.json")
# Function to save JSON data to a file
    def save_data_to_file(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")
# Initializing the class with the API URL and making API calls
    def __init__(self, api):
        self.get_data(api)

        parameters = {
            "search": "brand_name:aspirin AND product_type:OTC",
            "limit":10
        }
        self.get_user_data(api, parameters)

#Main function to create an instance of the MakeApiCall class and call the functions
if __name__ == "__main__":
    api_url = "https://api.fda.gov/drug/ndc.json?api_key=wKsgToU6B6Z3HgizK7KjUawgRKo5yRlaRBrMVvhP"

    MakeApiCall(api_url + "&search=brand_name:aspirin+product_type:OTC&limit=10")


# In[13]:


import pandas as pd
import json
# Open the JSON file and load its contents into the 'data' variable
with open('druglink3.json') as f:
    data = json.load(f)
    print(data)  # Debugging statement
# Use pandas to normalize the JSON data and create a DataFrame
df = pd.json_normalize(data['results'])
# Print the DataFrame for debugging purposes
print(df)  # Debugging statement
df.to_csv('drug_dataASCO.csv', index=False)


# In[ ]:




