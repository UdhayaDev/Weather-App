from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "d075ab1ccf0dba42f96ab6dd438f6371"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    print("POST received at /weather")  # Debugging
    data = request.get_json()
    if not data or "city" not in data:
        return jsonify({"error": "City not provided"}), 400

    city = data["city"].strip()
    if not city:
        return jsonify({"error": "City cannot be empty"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return jsonify({"error": "City not found"}), 404

    weather_data = {
        "city": response["name"],
        "temperature": response["main"]["temp"],
        "description": response["weather"][0]["description"],
        "icon": response["weather"][0]["icon"]
    }

    return jsonify(weather_data)


if __name__ == "__main__":
    app.run(debug=True)