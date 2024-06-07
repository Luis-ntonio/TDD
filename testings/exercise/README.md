# Documentation for Flask Application to Retrieve Coordinates

## Overview
This Python script sets up a Flask web application that provides an API endpoint to retrieve geographical coordinates (latitude and longitude) for a given query using the Nominatim service from OpenStreetMap.

## Dependencies
- Flask: A micro web framework for Python.
- requests: A simple HTTP library for Python.
- logging: Python's standard logging library.

## Files
- `myapp.log`: Log file to record application events and errors.

## Code Description

### Import Statements
```python
from flask import Flask, request, jsonify
import requests
import logging
```
- `Flask`: Importing the Flask class to create the web application.
- `request`: Importing to handle incoming HTTP requests.
- `jsonify`: Importing to convert Python dictionaries to JSON responses.
- `requests`: Importing to make HTTP requests to external APIs.
- `logging`: Importing to enable logging.

### Application Setup
```python
app = Flask(__name__)
logging.basicConfig(filename='./testings/exercise/myapp.log', level=logging.INFO)
```
- `app`: Initializing the Flask application.
- `logging.basicConfig`: Configuring the logging to write to `myapp.log` with the INFO level.

### Function to Get Coordinates
```python
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
```
- `get_coordinates(query)`: A function that takes a query string and returns the latitude and longitude as a tuple.
  - Checks if the query is `"not covered"` and returns a default coordinate `(1, 1)`.
  - Constructs a URL to query the Nominatim API with the provided query.
  - Sets a custom User-Agent header.
  - Makes a GET request to the Nominatim API and parses the JSON response.
  - Extracts the first result's latitude and longitude, rounds them to seven decimal places, and returns them as a tuple.
  - Handles exceptions and returns an error message as a string.

### API Endpoint
```python
@app.route('/get_coordinates', methods=['GET'])
def get_coordinates_endpoint():
    query = request.args.get('query')
    if not query:
        logging.error("Query parameter is required")
        return jsonify({"error": "Query parameter is required"}), 400
    result = get_coordinates(query)
    if isinstance(result, tuple):
        logging.info(f"Query: {query}, Result: {result}")
        return jsonify({"latitude": result[0], "longitude": result[1]})
    else:
        logging.error(f"Query: {query}, Error: {result}")
        return jsonify({"error": result}), 400
```
- `@app.route('/get_coordinates', methods=['GET'])`: Defines the `/get_coordinates` endpoint that accepts GET requests.
- `get_coordinates_endpoint()`: A function that handles incoming requests to the `/get_coordinates` endpoint.
  - Retrieves the `query` parameter from the request.
  - Logs an error and returns a JSON error response if the query parameter is missing.
  - Calls the `get_coordinates` function with the query parameter.
  - Logs the query and result, and returns a JSON response with the coordinates if successful.
  - Logs an error and returns a JSON error response if the `get_coordinates` function fails.

### Running the Application
```python
if __name__ == '__main__':
    app.run(debug=True)
```
- Runs the Flask application in debug mode if the script is executed directly.

## Usage
To use this application, send a GET request to the `/get_coordinates` endpoint with a `query` parameter containing the location name. The response will be a JSON object with the latitude and longitude of the queried location. If an error occurs, the response will contain an error message.

Example request:
```
GET /get_coordinates?query=New York
```

Example response:
```json
{
  "latitude": 40.712776,
  "longitude": -74.005974
}
```