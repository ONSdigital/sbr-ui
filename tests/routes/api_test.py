from sbr_ui import app


app.testing = True


# TODO: fix the tests below, they pass but they shouldn't as the routes are restrictred to logged in users


def test_get_by_id_type_period():
    with app.test_client() as c:
        api_response = c.get('/api/periods/201810/types/ENT/units/1', follow_redirects=True)
        assert api_response.status_code == 200


def test_search():
    with app.test_client() as c:
        api_response = c.get('/api/search_reference_number/1', follow_redirects=True)
        assert api_response.status_code == 200

