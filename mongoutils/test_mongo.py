def test_players(mongodb):
    assert 'players' in mongodb.collection_names()
    manuel = mongodb.players.find_one({'name': 'Manuel'})
    assert manuel['surname'] == 'Neuer'
