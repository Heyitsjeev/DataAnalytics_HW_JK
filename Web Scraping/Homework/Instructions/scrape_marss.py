#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests as req


# # Scrape everything
# 

# In[27]:


# this dictionary will hold everything we pull from all the sites
scraped_data = {}


# In[28]:


# site 1 -
news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest" # probably need to replace this since it redirects
newsResponse = req.get(news_url)

newsSoup = bs(newsResponse.text, "html.parser")
#print(newsSoup.prettify())

newsTitle = newsSoup.find("div", class_="content_title").text
scraped_data['news_title'] = newsTitle

newsPara = newsSoup.find("div", class_="rollover_description_inner").text
scraped_data['news_paragraph'] = newsPara


# In[29]:


# site 2 - https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

fimageWebUrl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(fimageWebUrl)

html = browser.html
imageSoup = bs(html, "html.parser")


# In[30]:


fimageUrlHtml = imageSoup.find("div", class_= "carousel_items").find("article")["style"].split("'")[1]
scraped_data['featured_image_url'] = fimageWebUrl + fimageUrlHtml
print(scraped_data['featured_image_url'])


# In[31]:


# site 3 - https://twitter.com/marswxreport?lang=en

twitterSite = req.get("https://twitter.com/marswxreport?lang=en")
twitterSoup = bs(twitterSite.text, 'html.parser')

tweetSiteInfo = twitterSoup.find_all('div', class_="js-tweet-text-container")
marsWeather = tweetSiteInfo[0].text
print(marsWeather)
scraped_data['Mars_Weather'] = marsWeather

#mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'


# In[32]:


# site 4 - 
marsFactsSite = "https://space-facts.com/mars/"
marsFacts = pd.read_html(marsFactsSite)
marsFacts_df = marsFacts[0]

marsFactsHtml = marsFacts_df.to_html(header = False, index = False)
scraped_data['Mars_Facts'] = marsFactsHtml
print(marsFactsHtml)


# In[36]:


# site 5 
# use bs4 to scrape the title and url and add to dictionary
# Example:
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

articleSite = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(articleSite)

HemsHtml = browser.html
soup = bs(HemsHtml, 'html.parser')


# In[37]:



marsHems=[]

for i in range (4):
    HemsImages = browser.find_by_tag('h3')
    HemsImages[i].click()
    html = browser.html
    hemSoup = bs(html, 'html.parser')
    partialHems = hemSoup.find("img", class_="wide-image")["src"]
    imgTitleHems = hemSoup.find("h2",class_="title").text
    imgUrlHems = 'https://astrogeology.usgs.gov'+ partialHems
    dictionaryHems={"title":imgTitleHems,"img_url":imgUrlHems}
    marsHems.append(dictionaryHems)
    
    browser.back()

scraped_data['Mars_Hem_Images'] = marsHems    
print(marsHems)


# In[ ]:


# File-> download as python into a new module called scrape_mars.py


# In[ ]:


# use day 3 09-Ins_Scrape_And_Render/app.py as a blue print on how to finish the homework.

# replace the contents of def index() and def scraper() appropriately.

# change the index.html to render the site with all the data.

