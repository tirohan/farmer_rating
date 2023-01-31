from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/data")
def get_data():
    with open("home/rohan/farmer_rating_system/latest_data3.json") as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
