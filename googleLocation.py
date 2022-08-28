#GoogleMaps API Key = AIzaSyDVWsvnDcZnUf18osOKKN79Gb3Tqg5NQwg
import json
from tkinter.messagebox import RETRY
import requests
import random

response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json")
# print(response.status_code)
# print(response.json)

# def parse_url_nearbysearch(long, lat, keyword):
def rand_url_nearbysearch():
    lat = random.randint(-90, 90)
    long = random.randint(-180, 180)
    radius = random.randint(30000, 50000)
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
    url += str(lat)
    url += "%2C"
    url += str(long)
    url += "&radius="
    url += str(radius)
    url += "&type=restaurant&key=AIzaSyDVWsvnDcZnUf18osOKKN79Gb3Tqg5NQwg"
    ret = [lat, long, url]
    return ret


# url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=45.8670522%2C-71.1957362&radius=100000000000&type=restaurant&key=AIzaSyDVWsvnDcZnUf18osOKKN79Gb3Tqg5NQwg"

def returnCoords():
    rounds = 0
    while(True):
        url = rand_url_nearbysearch()

        payload={}
        headers = {}

        response = requests.request("GET", url[2], headers=headers, data=payload)

        # print(response.text)
        # print("\n\n\n\n\n\n\nNew\n\n\n\n\n")
        # print(type(response))
        
        jsonResponse = response.json()
        # print(response.text)
        # print(type(jsonResponse["results"]))
        # print("\n\n\n\n\n\n\nNew\n\n\n\n\n")
        rounds +=1
        if(jsonResponse["status"] == "ZERO_RESULTS"):
            continue
        elif(len(jsonResponse["results"])>5):
            break

    i=0
    print(response.json()["results"][0]["geometry"]["location"])
    ret = []
    ret.append([url[0], url[1]])
    while(i<5):
        line = []
        line.append(jsonResponse["results"][i]["name"])
        line.append(jsonResponse["results"][i]["geometry"]["location"]["lat"])
        line.append(jsonResponse["results"][i]["geometry"]["location"]["lng"])
        line.append(i)
        # print(jsonResponse["results"][i]["name"]) # fetches the name of 1st entry of the results
        # print(line)
        ret.append(line)
        i += 1
    print(ret)
    jsret = json.dumps(ret)
    print("\n")
    print(rounds)
    return jsret

returnCoords()