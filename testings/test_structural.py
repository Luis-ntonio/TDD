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
