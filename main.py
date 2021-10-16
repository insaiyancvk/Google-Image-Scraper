# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
from GoogleImageScrapper import GoogleImageScraper
import os


if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")
    image_path = os.path.normpath(os.getcwd()+"\\photos")

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys= [
        'Chichi dragon ball OR Z OR super OR fanart',
        'Frieza dragon ball OR Z OR super OR fanart',
        'Kuririn dragon ball OR Z OR super OR fanart',
        'Piccolo dragon ball OR Z OR super OR fanart',
        'Son Gohan dragon ball OR Z OR super OR fanart',
        'Son Goku dragon ball OR Z OR super OR fanart',
        'Trunks dragon ball OR Z OR super OR fanart',
        'Vegeta dragon ball OR Z OR super OR fanart'
        ]

    #Parameters
    number_of_images = 500
    headless = False
    min_resolution=(0,0)
    max_resolution=(9999,9999)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)
    
    #Release resources    
    del image_scrapper