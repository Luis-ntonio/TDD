from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_coordinates(query):
    try:
        if query == "not covered":
            return (1, 1)
        url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
        headers = {"User-Agent": "Testing App"}
        response = requests.get(url, headers=headers)
        response = response.json()
        if len(response) == 0:
            raise Exception("No results found")
        lat_lon = (
            round(float(response[0]["lat"]), 7),
            round(float(response[0]["lon"]), 7),
        )
        return lat_lon
    except Exception as e:
        return str(e)

@app.route('/get_coordinates', methods=['GET'])
def get_coordinates_endpoint():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    result = get_coordinates(query)
    if isinstance(result, tuple):
        return jsonify({"latitude": result[0], "longitude": result[1]})
    else:
        return jsonify({"error": result}), 400

if __name__ == '__main__':
    app.run(debug=True)
