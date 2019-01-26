from flask import Flask,render_template,jsonify
from flask_cors import CORS

from rattyscraper import Scraper

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    s = Scraper()
    return jsonify(s.scrapeRatty())

if __name__ == '__main__':
    app.run()