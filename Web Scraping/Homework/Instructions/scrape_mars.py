# Importing dependencies
from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests
from flask import Flask, render_template
import time
import numpy as np
import json
from selenium import webdriver


def init_browser():
    # splinter
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    mars = {}

    # site 1 -
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest" # probably need to replace this since it redirects
    newsResponse = req.get(news_url)

    newsSoup = bs(newsResponse.text, "html.parser")
    #print(newsSoup.prettify())

    newsTitle = newsSoup.find("div", class_="content_title").text
    mars["news_title"] = newsTitle

    newsPara = newsSoup.find("div", class_="rollover_description_inner").text
    mars['news_paragraph'] = newsPara

    # site 2 - https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    init_browser()

    fimageWebUrl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(fimageWebUrl)

    html = browser.html
    imageSoup = bs(html, "html.parser")

    fimageUrlHtml = imageSoup.find("div", class_= "carousel_items").find("article")["style"].split("'")[1]
    mars['featured_image_url'] = fimageWebUrl + fimageUrlHtml
    print(mars['featured_image_url'])

    # site 3 - https://twitter.com/marswxreport?lang=en

    twitterSite = req.get("https://twitter.com/marswxreport?lang=en")
    twitterSoup = bs(twitterSite.text, 'html.parser')

    tweetSiteInfo = twitterSoup.find_all('div', class_="js-tweet-text-container")
    marsWeather = tweetSiteInfo[0].text
    print(marsWeather)
    mars['Mars_Weather'] = marsWeather

    # site 4 - 
    marsFactsSite = "https://space-facts.com/mars/"
    marsFacts = pd.read_html(marsFactsSite)
    marsFacts_df = marsFacts[0]

    marsFactsHtml = marsFacts_df.to_html(header = False, index = False)
    mars['Mars_Facts'] = marsFactsHtml
    print(marsFactsHtml)

    articleSite = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(articleSite)

    HemsHtml = browser.html
    soup = bs(HemsHtml, 'html.parser')
    
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

    mars['Mars_Hem_Images'] = marsHems    
    print(marsHems)

    return mars