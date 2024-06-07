import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_can_call_existing_endpoints_of_the_API():
    response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': 'Lima,Peru'})
    assert response.status_code == 200

def test_cannot_call_non_existing_endpoints_of_the_API():
    response = requests.get(f'{BASE_URL}/non_existing_endpoint')
    assert response.status_code == 404

def test_endpoint_returns_something():
    response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': 'Lima,Peru'})
    assert response.json() is not None

def test_the_result_is_correct_for_simple_cases():
    response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': 'Lima,Peru'})
    data = response.json()
    assert (data['latitude'], data['longitude']) == (-12.0621065, -77.0365256)

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

def test_result_not_found_results():
    response = requests.get(f'{BASE_URL}/get_coordinates', params={'query': 'abcdefghijklmnoqrstuvwxyz'})
    data = response.json()
    assert "No results found" in data['error']
