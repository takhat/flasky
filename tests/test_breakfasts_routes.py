# test empty database

def test_get_all_breakfasts_with_empty_database_returns_empty_list(client):
    #Arrange
    response = client.get('/breakfast')
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_breakfast_with_empty_database_returns_404(client):
    response = client.get('/breakfast/1')
    response_body = response.get_json()

    assert response.status_code == 404

    assert "msg" in response_body

def test_get_one_breakfast_with_populated_db_returns_breakfast_json(client, two_breakfasts):
    #Arrange
    response = client.get('/breakfast/1')
    response_body = response.get_json()
    
    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Pancakes",
        "rating": 3.5,
        "prep_time": 20
    }

def test_post_one_breakfast_creates_breakfast_in_db(client, two_breakfasts):
    #Arrange
    response = client.post('/breakfast', json={
        "name": "Bread Butter",
        "rating": 4,
        "prep_time": 5
    })
    response_body = response.get_json()
    #Assert
    assert response.status_code == 201
    #assert "id" in response_body
    assert "id" in response_body["msg"]
    # assert response_body["name"] == "Bread Butter"
    # assert response_body["rating"] == 4
    # assert response_body["prep_time"] == 5







