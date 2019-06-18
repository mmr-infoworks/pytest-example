import pytest
mongodbc = None
ss = None

mongodbc = None

def test_tables(mongodb):
    set_mongo(mongodb)
    assert 'tables' in mongodb.collection_names()
    table = mongodb.tables.find_one({})
    assert table['table'] == 'weather'
    assert str(table['_id']) == '59787de7e4b0710ef3d97fb6'
    assert str(table['_id']) != '58787de7e4b0710ef3d97fb6'
    assert mongodbc == mongodb

def test_update(mongodb):
    print ("hiii")
    set_mongo(mongodb)
    mongodb.tables.update({},{'$set':{'f1':'newfield'}})
    table = mongodb.tables.find_one({})
    assert table['f1'] == 'newfield'
    assert mongodbc == mongodb
    
def set_mongo(mongo):
    global mongodbc
    mongodbc = mongo