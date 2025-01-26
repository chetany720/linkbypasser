from flask import Flask, request, redirect, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bypass', methods=['POST'])
def bypass():
    url = request.form['url']
    try:
        # Follow redirects to find the final URL
        response = requests.get(url, allow_redirects=True)
        return redirect(response.url)
    except requests.RequestException:
        return "Error bypassing the link."

if __name__ == '__main__':
    app.run(debug=True)