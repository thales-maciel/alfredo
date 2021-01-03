def test_left_space_is_removed_from_query(alfredo):
    _, query = alfredo.parse_query('   test')
    assert 'test' == query


def test_number_brings_calculator(alfredo):
    plugin, _ = alfredo.parse_query('12')
    assert alfredo.calculator == plugin

