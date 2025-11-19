from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# ------------------------------
# Roboflow Public Skin Model
# ------------------------------

API_KEY = "kTK0gAawSv3eqEDeXfAs"    # your API key
MODEL_ENDPOINT = "https://detect.roboflow.com/skin-disease-8class/1"


@app.route("/")
def dash():
    return render_template('analyze.html')


@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"})

        file = request.files['file']

        # save file temporarily
        temp_path = "temp.jpg"
        file.save(temp_path)

        # send request to Roboflow
        url = f"{MODEL_ENDPOINT}?api_key={API_KEY}"
        response = requests.post(url, files={'file': open(temp_path, 'rb')})

        # remove temp file
        os.remove(temp_path)

        try:
            return jsonify(response.json())
        except:
            return jsonify({"error": "Prediction failed"})


    return render_template('app.html')


@app.route('/favicon.ico')
def favicon():
    return jsonify({"msg": "ok"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
