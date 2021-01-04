import pytest


def test_query_works_with_string(alfredo):
    """Str is allowed in query"""
    _, query = alfredo.parse_query('test')
    assert 'test' == query


def test_only_strings_allowed(alfredo):
    """Only str should be allowed in the query"""
    with pytest.raises(TypeError):
        alfredo.parse_query(12)


def test_left_space_is_removed_from_query(alfredo):
    """Leading space should be ignored in the query"""
    _, query = alfredo.parse_query('   test')
    assert 'test' == query


def test_number_brings_calculator(alfredo):
    """If a query can be evaluated the calculator
    plugin should be selected"""
    plugin, _ = alfredo.parse_query('12')
    assert alfredo.calculator == plugin

