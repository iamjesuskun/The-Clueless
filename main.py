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
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)