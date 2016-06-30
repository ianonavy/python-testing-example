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
