import pytest

from alfredo.core import Alfredo

@pytest.fixture
def alfredo():
    return Alfredo(None)
