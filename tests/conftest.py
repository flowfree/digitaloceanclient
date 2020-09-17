import json

import pytest

from digitaloceanclient import DigitalOceanClient


@pytest.fixture
def client():
    return DigitalOceanClient('TEST_TOKEN')


@pytest.fixture
def load_json():
    def func(fixture_name):
        filename = f'tests/fixtures/{fixture_name}'
        with open(filename) as f:
            return json.load(f)
    return func
