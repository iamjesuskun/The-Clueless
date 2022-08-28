from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)