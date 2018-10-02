from sbr_ui import app

app.testing = True


# TODO: fix the tests to login first


def test_get_by_id_type_period():
    with app.test_client() as c:
        api_response = c.get('/Search/periods/201810/types/ENT/units/1', follow_redirects=True)
        assert api_response.status_code == 200


def test_search():
    with app.test_client() as c:
        api_response = c.get('/Search', follow_redirects=True)
        assert api_response.status_code == 200

