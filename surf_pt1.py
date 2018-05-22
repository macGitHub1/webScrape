# Module used to connect Python with MongoDb
from bs4 import BeautifulSoup as bs
import requests
from lxml import html
from datetime import datetime
import pymongo

#datase set-up
#setup mongo
# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# Define database and collection
db = client.surf_db
collection = db.items

#web target
web_target = "https://www.surfline.com/surf-reports-forecasts-cams/costa-rica/3624060"
web_base = "https://surfline.com"

def main():
    page = requests.get(web_target)

    # Create a Beautiful Soup object
    soup = bs(page.text, 'html.parser')

    # results 
    results = soup.find_all('div', class_ = "sl-spot-list__ref")
    dictList = []
    for result in results:
      temp_dictionary = {}
      try:
        
        #result = soup.find('div', class_="sl-spot-details")
        temp_dictionary["location"] = result.find("h3",  class_ = "sl-spot-details__name").text
        temp_dictionary["height"]  = result.find("span", class_ = "quiver-surf-height").text
        temp_dictionary["url"] =  str (web_base + result.a["href"])
        #get_water_air_temp(url = str(web_base + result.a["href"]) )
        temp_dictionary ["date"] =  "{:%d.%m.%Y}".format(datetime.now())
        collection.insert_one(temp_dictionary)        
        
        
      except AttributeError as e:
       go_silent = e
      dictList.append(temp_dictionary)
    

def get_water_air_temp(url): #return a dictionary
    url = url
    out = { 'air': "None", 'water': "None"}
    page = requests.get(url)
    soup1 = bs(page.text, 'html.parser')
    
    results = soup1.find('div', class_ = "sl-weather-graph__temperature").text
    
   
    return (out)



if __name__ == "__main__":
    main()
    
