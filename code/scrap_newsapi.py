#!/usr/bin/env python3
# coding: utf-8

# In[57]:

# news api 
import requests
from datetime import datetime
import pandas as pd
from datetime import date 
from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup


# In[58]:


api_key = "b7cd9a15f6ba4979ab21c3d0317948c3"

print(api_key)
# In[59]:


# Function to scrape the main text from <p> tags of an article
def scrape_article_text(url):
    try:
        # Send a request to the URL
        response = requests.get(url,  timeout=5)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all the <p> tags and extract the text
            paragraphs = soup.find_all('p')
            text = ' '.join([para.get_text() for para in paragraphs])
            
            return text.strip()  # Return the cleaned text
        else:
            return f"Failed to retrieve article: {response.status_code}"
    
    except Exception as e:
        return f"Error occurred: {str(e)}"


# In[60]:


# Function to fetch top headlines in the United States
def get_top_headlines(country, base_path, api_key):
    
    # parameters
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
            'country': 'us',  # for US headlines
            'apiKey': api_key,
            'pageSize': 100
        }
    
    # macros
    # creating the date object of today's date 
    todays_date = date.today()

    # time
    todays_time = datetime.now().strftime('%H-%M')

    # Send the request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # save
    filename = country + "_" + str(todays_date) + "_" + str(todays_time) + ".json"

    # add date
    [a.update({"date": str(todays_date)}) for a in articles]
    
    # add text of the article
    for article in articles:
        # scrape
        print("Downloading " + article["url"])
        article["content"] = scrape_article_text(article["url"])
    
    # Convert the dictionary to JSON and save it to the file
    with open(f'{base_path}/{filename}', "w") as json_file:
            json.dump(articles, json_file)
    
    print("saving" + f'{base_path}/{filename}')
    
    return articles        

# Call the function
get_top_headlines(country="US", base_path="/Users/tb186/dropbox/artigos/VVW_LLMs_urls/news_us", api_key=api_key)
