import pytest
import mock
from conftest import my_vcr

from favorite_printer.main import *


def test_count_favorite_colors_counts_colors():
    favorite_colors = {
        'Kyle': "Green",
        'Elize': "Green",
        'Chris': "Blue",
        'Connor': "Blue",
    }
    actual = count_favorite_colors(favorite_colors)
    expected = Counter({
        'Green': 2,
        'Blue': 2,
    })
    assert expected == actual


def test_parse_people_returns_list_when_no_data():
    example_input = '{"persons":[]}'
    assert [] == parse_people(example_input)


def test_parse_people_returns_list_of_dicts(raw_data):
    expected = [
        {"favoriteColor": "Yellow", "name": "Alice"},
        {"favoriteColor": "Green", "name": "Bob"},
        {"favoriteColor": "Red", "name": "Charlie"},
        {"favoriteColor": "Red", "name": "Dean"},
        {"favoriteColor": "Yellow", "name": "Eve"}
    ]
    assert expected == parse_people(raw_data)


def test_parse_people_raises_exception_for_invalid_data(invalid_raw_data):
    with pytest.raises(ValueError):
        parse_people(invalid_raw_data)


def test_parse_people_supports_v2(raw_data_v2):
    assert 5 == len(parse_people(raw_data_v2))


@mock.patch('requests.get')
def test_get_raw_people_uses_version_header(mock_requests_get):
    get_raw_people_data()
    args, kwargs = mock_requests_get.call_args_list[0]
    assert 'FAVORITE-API-VERSION' in kwargs['headers']


@mock.patch('requests.get')
def test_get_raw_people_uses_version_header_v2(mock_requests_get):
    get_raw_people_data(version='v2')
    args, kwargs = mock_requests_get.call_args_list[0]
    assert {'FAVORITE-API-VERSION': 'v2'} == kwargs['headers']


@my_vcr.use_cassette
def test_get_raw_people_data_contains_persons():
    assert "persons" in get_raw_people_data()
