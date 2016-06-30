"""Summarizes and prints the favorite colors base on data from an API.

Motivating example for testing in Python.

"""

import json
from collections import Counter

import requests


SERVER_URL = 'http://localhost:5000/'
COLOR_COUNT_TEMPLATE = """- {color}: {count}"""
SUMMARY_TEMPLATE = """People's favorite colors:

{color_counts}
"""


def count_favorite_colors(favorite_colors):
    """Counts everyone's favorite colors

    :param dict favorite_colors: Mapping of names to favorite colors
    :return: Mapping of colors to counts
    :rtype: :class:`collections.Counter`
    """
    return Counter(favorite_colors.values())


def format_color_counts(counts):
    """Formats the partial summary of favorite color counts

    :param dict counts: Mapping of colors to a count of people with
        that color as their favorite
    :return str: Template partial for summarized favorite color counts
    """
    return '\n'.join([
        COLOR_COUNT_TEMPLATE.format(color=color, count=count)
        for color, count in counts.items()
    ])


def get_raw_people_data(version='v1'):
    """Fetches the raw data.

    :param str version: Version of the API to use
    :return str: Raw API response
    """
    headers = {
        'FAVORITE-API-VERSION': version,
    }
    return requests.get(SERVER_URL, headers=headers).text


def parse_people(raw_data):
    """Parses the list of people from the raw data

    Example:

    [
        {
            'name': "Ian",
            'favoriteColor': "Purple",
        },
        {
            'name': "Lekha",
            'favoriteColor': "Red",
        }
    ]

    :param str raw_data: The serialized raw response from the API
    :return list: List of deserialized dicts of people
    :raises ValueError: raw_data is not valid JSON
    :raises KeyError: raw data
    """
    return json.loads(raw_data)['persons']


def summarize_favorite_colors(people):
    """Counts and summarizes

    :param dict people: List of dictionaries related to people metadata
        from the API
    :return str: Summary message of favorite color counts
    """
    favorite_colors = {
        person['name']: person['favoriteColor']
        for person in people
    }
    counts = count_favorite_colors(favorite_colors)
    color_counts = format_color_counts(counts)
    return SUMMARY_TEMPLATE.format(color_counts=color_counts)


def main():
    """Summarizes the favorite from a raw API of people data."""
    raw_data = get_raw_people_data()
    people = parse_people(raw_data)
    print(summarize_favorite_colors(people))


if __name__ == '__main__':
    main()
