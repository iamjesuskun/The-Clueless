from flask import Flask, render_template
import json
import requests
import random

app = Flask(__name__)
#GoogleMaps API Key = AIzaSyDVWsvnDcZnUf18osOKKN79Gb3Tqg5NQwg

@app.route("/")
def home():
    return render_template('home.html')
@app.route('/about', methods=['GET', 'POST'])
def about():
    # if request.method == 'POST':
    return render_template('about.html')
    
@app.route('/countries', methods=['GET', 'POST'])
def countries():
    return render_template('countries.html')

@app.route('/Asia', methods=['GET', 'POST'])
def asia():
    return render_template('continents/asia.html')

@app.route('/Europe', methods=['GET', 'POST'])
def europe():
    return render_template('continents/europe.html')

@app.route('/SouthAmerica', methods=['GET', 'POST'])
def south_america():
    return render_template('continents/sa.html')

@app.route('/NorthAmerica', methods=['GET', 'POST'])
def north_america():
    return render_template('continents/na.html')

@app.route('/Africa', methods=['GET', 'POST'])
def africa():
    return render_template('continents/africa.html')

@app.route('/Pacific', methods=['GET', 'POST'])
def pacific():
    return render_template('continents/pacific.html')

@app.route('/Randomized', methods=['GET', 'POST'])

def randomized():
    return render_template('Randomized.html')


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
@app.route('/index')
def returnCoords():
    response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json")
    rounds = 0
    while(True):
        url = rand_url_nearbysearch()

        payload={}
        headers = {}

        response = requests.request("GET", url[2], headers=headers, data=payload)
        
        jsonResponse = response.json()
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
        line.append(i+1)
        # print(jsonResponse["results"][i]["name"]) # fetches the name of 1st entry of the results
        # print(line)
        ret.append(line)
        i += 1
    print(ret)
    jsret = json.dumps(ret)
    print("\n")
    print(rounds)
    return render_template('searchresults/index.html', array=ret)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)