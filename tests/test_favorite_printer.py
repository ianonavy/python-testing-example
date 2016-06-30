from conftest import my_vcr

from favorite_printer.main import *


def test_parse_people_supports_v2():
    v2_example_input = """
{
  "people": [
    {
      "favoriteColor": "Green",
      "favoritePizza": "Veggie",
      "name": "Alice"
    },
    {
      "favoriteColor": "Red",
      "favoritePizza": "Pepperoni",
      "name": "Bob"
    },
    {
      "favoriteColor": "Green",
      "favoritePizza": "Meat Lover's",
      "name": "Charlie"
    },
    {
      "favoriteColor": "Red",
      "favoritePizza": "Cheese",
      "name": "Dean"
    },
    {
      "favoriteColor": "Blue",
      "favoritePizza": "Veggie",
      "name": "Eve"
    }
  ]
}

"""
    assert len(parse_people(v2_example_input)) == 5


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
