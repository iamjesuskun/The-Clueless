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

@app.route('/asia', methods=['GET', 'POST'])
def asia():
    return render_template('continents/asia.html')

@app.route('/europe', methods=['GET', 'POST'])
def europe():
    return render_template('continents/europe.html')

@app.route('/south america', methods=['GET', 'POST'])
def south_america():
    return render_template('continents/sa.html')

@app.route('/north america', methods=['GET', 'POST'])
def north_america():
    return render_template('continents/na.html')

@app.route('/africa', methods=['GET', 'POST'])
def africa():
    return render_template('continents/africa.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)