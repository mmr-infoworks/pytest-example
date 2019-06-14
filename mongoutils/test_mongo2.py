def test_tables(mongodb):
    assert 'tables' in mongodb.collection_names()
    table = mongodb.tables.find_one({})
    assert table['table'] == 'weather'
    assert str(table['_id']) == '59787de7e4b0710ef3d97fb6'
    assert str(table['_id']) != '58787de7e4b0710ef3d97fb6'
