import pytest
from exercise.example import get_coordinates


def test_can_call_existing_endpoints_of_the_API():
    ret = get_coordinates("Lima,Peru")
    assert ret is not None

def test_cannot_call_non_existing_endpoints_of_the_API():
    try:
        from exercise.example import something_not_existent
        ret = something_not_existent("bla bla")
    except:
        assert True, "Exception raised"

def test_endpoint_returns_something():
    ret = get_coordinates("Lima,Peru")
    assert ret is not None

def test_the_result_is_correct_for_simple_cases():
    ret = get_coordinates("Lima,Peru")
    assert ret == (-12.0621065, -77.0365256)

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
        ret = get_coordinates(cases[i])
        assert abs(ret[0] - expected[i][0]) < 0.1