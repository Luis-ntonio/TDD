# Documentation for API Testing with Pytest

## Overview
This Python script contains a set of pytest-based tests to verify the functionality of a Flask web application's API. The tests interact with the `/get_coordinates` endpoint to ensure it behaves correctly under various scenarios.

## Dependencies
- pytest: A framework for testing Python applications.
- requests: A simple HTTP library for Python.

## Base URL
- `BASE_URL`: The base URL of the Flask web application, set to `http://127.0.0.1:5000`.

## Tests

### Import Statements
```python
import pytest
import requests
```
- `pytest`: Importing the pytest framework for writing and running tests.
- `requests`: Importing to make HTTP requests to the API.

### Base URL Configuration
```python
BASE_URL = 'http://127.0.0.1:5000'
```
- `BASE_URL`: Defines the base URL of the Flask web application.

### Test Cases

#### 1. Test Existing Endpoint Accessibility
```python
def test_can_call_existing_endpoints_of_the_API():
    response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': 'Lima,Peru'})
    assert response.status_code == 200
```
- `test_can_call_existing_endpoints_of_the_API()`: Tests if the `/get_coordinates` endpoint is accessible and returns a 200 status code.

#### 2. Test Non-existing Endpoint Accessibility
```python
def test_cannot_call_non_existing_endpoints_of_the_API():
    response = requests.get(f'{BASE_URL}/non_existing_endpoint')
    assert response.status_code == 404
```
- `test_cannot_call_non_existing_endpoints_of_the_API()`: Tests if a non-existing endpoint returns a 404 status code.

#### 3. Test Endpoint Returns Response
```python
def test_endpoint_returns_something():
    response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': 'Lima,Peru'})
    assert response.json() is not None
```
- `test_endpoint_returns_something()`: Tests if the `/get_coordinates` endpoint returns a non-null JSON response.

#### 4. Test Correctness of Simple Case Result
```python
def test_the_result_is_correct_for_simple_cases():
    response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': 'Lima,Peru'})
    data = response.json()
    assert (data['latitude'], data['longitude']) == (-12.0621065, -77.0365256)
```
- `test_the_result_is_correct_for_simple_cases()`: Tests if the `/get_coordinates` endpoint returns the correct coordinates for "Lima,Peru".

#### 5. Test Correctness for Multiple Inputs
```python
def test_the_result_is_correct_for_all_inputs():
    cases = [
        "Lima,Peru",
        "New York,USA",
        "Paris,France",
        "not covered",
        "Berlin,Germany",
        "Tokyo,Japan",
    ]
    expected = [
        (-12.0621065, -77.0365256),
        (40.7127281, -74.0060152),
        (48.8588897, 2.320041),
        (1, 1),
        (52.5170365, 13.3888599),
        (35.6821936, 139.762221),
    ]
    for i in range(len(cases)):
        response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': cases[i]})
        data = response.json()
        assert abs(data['latitude'] - expected[i][0]) < 0.1
        assert abs(data['longitude'] - expected[i][1]) < 0.1
```
- `test_the_result_is_correct_for_all_inputs()`: Tests if the `/get_coordinates` endpoint returns approximately correct coordinates for a variety of queries. The results are checked within a tolerance of 0.1 degrees.

#### 6. Test Result Not Found Handling
```python
def test_result_not_found_results():
    response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': 'abcdefghijklmnoqrstuvwxyz'})
    data = response.json()
    assert "No results found" in data['error']
```
- `test_result_not_found_results()`: Tests if the `/get_coordinates` endpoint returns an appropriate error message when no results are found for the given query.

## Running the Tests
To run these tests, execute the following command in the terminal:
```sh
pytest
```
This command will execute all the test functions defined in the script and report the results.