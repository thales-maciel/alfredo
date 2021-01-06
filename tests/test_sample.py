import pytest


def test_query_works_with_string(fredo):
    """Str is allowed in query"""
    _, query = fredo.parse_query('test')
    assert 'test' == query


def test_only_strings_allowed(fredo):
    """Only str should be allowed in the query"""
    with pytest.raises(TypeError):
        fredo.parse_query(12)


def test_left_space_is_removed_from_query(fredo):
    """Leading space should be ignored in the query"""
    _, query = fredo.parse_query('   test')
    assert 'test' == query


def test_number_brings_calculator(fredo):
    """If a query can be evaluated the calculator
    plugin should be selected"""
    plugin, _ = fredo.parse_query('12')
    assert fredo.calculator == plugin
