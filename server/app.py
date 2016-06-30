"""Server implementation for motivating example.

This code is terrible. Don't use it for any sort of example.

"""

import random

from flask import Flask, jsonify, request, session


ERROR_MODE = False


NAMES = [
    'Alice',
    'Bob',
    'Charlie',
    'Dean',
    'Eve',
]
COLORS = [
    'Red',
    'Orange',
    'Yellow',
    'Green',
    'Blue',
]
PIZZAS = [
    'Cheese',
    'Pepperoni',
    'Veggie',
    'Meat Lover\'s',
    'Hawaiian',
]

app = Flask(__name__)
count = 0


def get_data_v1():
    return {
        'persons': [
            {
                'name': name,
                'favoriteColor': random.choice(COLORS)
            }
            for name in NAMES
        ]
    }


def get_data_v2():
    return {
        'people': [
            {
                'name': name,
                'favoriteColor': random.choice(COLORS),
                'favoritePizza': random.choice(PIZZAS),
            }
            for name in NAMES
        ]
    }


@app.route('/')
def index():
    global count
    count = (count + 1) % 5
    if ERROR_MODE or count == 0:
        return 'An internal error has occured.', 500
    get_data_funcs = {
        'v1': get_data_v1,
        'v2': get_data_v2,
    }
    version = request.headers.get('FAVORITE-API-VERSION', 'v1')
    get_data = get_data_funcs.get(version)
    return jsonify(get_data())


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'test'
    app.run('0.0.0.0', debug=True)
