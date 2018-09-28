from sbr_ui import app


app.testing = True


# TODO: fix the tests below, they pass even with incorrect values which shouldn't be possible


def test_login():
    with app.test_client() as c:
        login_response = c.post('/auth/login', data={
            "username": "admin",
            "password": "admin",
        }, follow_redirects=True, headers={"content-type": "application/x-www-form-urlencoded"})
        assert login_response.status_code == 200
        logout_response = c.post('/auth/logout', follow_redirects=True)
        assert logout_response.status_code == 200


def test_logout():
    """ This test really shouldn't work as a new context is being used and to log out you have to be logged in.  """
    with app.test_client() as c:
        logout_response = c.post('/auth/logout', follow_redirects=True)
        assert logout_response.status_code == 200
