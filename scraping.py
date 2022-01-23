import requests
from configparser import ConfigParser
import lxml
from bs4 import BeautifulSoup


config = ConfigParser()
config.read("config.ini")


def car_features(keys):
    r = requests.get(config["DEFAULT"]["url"], params = keys)
    soup = BeautifulSoup(r.content, "lxml")
    liste = soup.find_all("div", {"class": "vehicle-card"}) # Car divs
    data = []
    for features in liste:
        title = features.find("h2", {"class": "title"}).text
        price = features.find("span", {"class": "primary-price"}).text
        year = features.find("h2", {"class": "title"}).text.split()[0]
        brand = features.find("h2", {"class": "title"}).text.split()[1]
        img_url = features.find("div", {"data-index": 0}).find("img").get("data-src", features.find("div", {"data-index": 0}).find("img").get("src"))
        link = features.find("a", {"class": "vehicle-card-link"}).get("href") # Car detail HREF
        car_deatils_link = ("https://www.cars.com/" + link)
        car_details(car_deatils_link)
        transmission = car_details(car_deatils_link)[1]
        color = car_details(car_deatils_link)[0]

        data.append({"Title": title , "Price": price, "Year": year, "Brand": brand,  "Img_url": img_url, "Transmission": transmission, "Exterior": color})


    return data

def car_details(car_deatils_link):
    r = requests.get(car_deatils_link)
    soup1 = BeautifulSoup(r.content, "lxml")
    
    car = soup1.find("dl", {"class", "fancy-description-list"}).find_all("dd") #car[0] -- Color // car[5]-- transmission
    return [car[0].text,car[5].text]

