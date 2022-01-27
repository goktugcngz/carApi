from flask import Flask, jsonify, request
from configparser import ConfigParser

from scraping import car_features

config = ConfigParser()
config.read("config.ini")

app = Flask(__name__)

@app.route("/")
def car_list():
    year = request.args.get("year")
    extcolor = request.args.get("extcolor")
    trans = request.args.get("trans")
    brand = request.args.get("brand")
    keys = {
        "year_max": year,
        "year_min": year,
        "exterior_color_slugs[]": extcolor,
        "page_size": config["DEFAULT"]["page_size"],
        "page": config["DEFAULT"]["page"],
        "makes[]": brand,
        "transmission_slugs[]": trans
    }

    return jsonify(car_features(keys))
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
