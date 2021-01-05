import pytest

from fredo.core import Fredo


@pytest.fixture
def fredo():
    return Fredo(None)
