import pytest
import vcr

my_vcr = vcr.VCR(
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
    cassette_library_dir='fixtures/cassettes',
    record_mode='once',
    match_on=['uri', 'method'],
)


@pytest.fixture
def raw_data():
    return """
{
  "persons": [
    {
      "favoriteColor": "Yellow",
      "name": "Alice"
    },
    {
      "favoriteColor": "Green",
      "name": "Bob"
    },
    {
      "favoriteColor": "Red",
      "name": "Charlie"
    },
    {
      "favoriteColor": "Red",
      "name": "Dean"
    },
    {
      "favoriteColor": "Yellow",
      "name": "Eve"
    }
  ]
}
"""


@pytest.fixture
def invalid_raw_data():
    return """
{
  "persons": [
    {
      "favoriteColor": "Yellow",
      "name": "Alice"
    },
    {
      "favoriteColor": "Green",
      "name": "Bob"
    },
    {
      "favoriteColor": "Red",
      "name": "Charlie"
    },
    {
      "favoriteColor": "Red",
      "name": "Dean"
    },
    {
      "favoriteColor": "Yellow",
      "name": "Eve"
    }
  ]

"""


@pytest.fixture
def raw_data_v2():
    return """
    {
  "people": [
    {
      "favoriteColor": "Red",
      "favoritePizza": "Cheese",
      "name": "Alice"
    },
    {
      "favoriteColor": "Red",
      "favoritePizza": "Cheese",
      "name": "Bob"
    },
    {
      "favoriteColor": "Green",
      "favoritePizza": "Meat Lover's",
      "name": "Charlie"
    },
    {
      "favoriteColor": "Red",
      "favoritePizza": "Meat Lover's",
      "name": "Dean"
    },
    {
      "favoriteColor": "Green",
      "favoritePizza": "Pepperoni",
      "name": "Eve"
    }
  ]
}"""