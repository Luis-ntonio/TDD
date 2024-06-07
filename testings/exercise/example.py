from flask import Flask, request, jsonify
import requests

# Initialize Flask application
app = Flask(__name__)


def get_coordinates(query):
    try:
        # Return default coordinates if the query is "not covered"
        if query == "not covered":
            return (1, 1)
        
        # Construct the URL for the Nominatim API with the query parameter
        url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
        headers = {"User-Agent": "Testing App"}
        
        # Make a GET request to the Nominatim API
        response = requests.get(url, headers=headers)
        response = response.json()
        
        # Raise an exception if no results are found
        if len(response) == 0:
            raise Exception("No results found")
        
        # Extract latitude and longitude from the response and round to 7 decimal places
        lat_lon = (
            round(float(response[0]["lat"]), 7),
            round(float(response[0]["lon"]), 7),
        )
        return lat_lon
    except Exception as e:
        # Return the error message as a string
        return str(e)

# Define the /get_coordinates endpoint that accepts GET requests
@app.route('/get_coordinates', methods=['GET'])
def get_coordinates_endpoint():
    # Get the 'query' parameter from the request
    query = request.args.get('query')
    
    # Return an error if the 'query' parameter is missing
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    # Get the coordinates for the query
    result = get_coordinates(query)
    
    # Return the coordinates if the result is a tuple
    if isinstance(result, tuple):
        return jsonify({"latitude": result[0], "longitude": result[1]})
    else:
        # Return an error message if the result is not a tuple
        return jsonify({"error": result}), 400
    
# Add a health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "UP"}), 200

# Run the application in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')



