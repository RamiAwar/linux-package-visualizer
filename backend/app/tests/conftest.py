import os

import pytest


@pytest.fixture()
def example_data():
    with open("app/tests/example_data.txt") as f:
        yield f.readlines()
