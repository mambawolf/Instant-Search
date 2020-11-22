#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import requests, webbrowser
from bs4 import BeautifulSoup

user_input = input("Enter The Search Text: ")
print("Searching.....")

google_search = requests.get("https://www.google.com/search?q=" + user_input)

soup = BeautifulSoup(google_search.text, 'html.parser')

search_results = soup.select('.eZt8xd')

for link in search_results[:5]:
    actual_link = link.get('href')
    webbrowser.open('https://google.com/' + actual_link)

print("process executed")   


# In[ ]:




