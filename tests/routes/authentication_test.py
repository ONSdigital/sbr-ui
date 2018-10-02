from sbr_ui import create_application


app = create_application()
app.testing = True


# TODO: fix tests below, the response is 200 even if the login failed, due to rendering of a template returning 200


def test_login():
    with app.test_client() as c:
        login_response = c.post('/Login', data={
            "username": "admin",
            "password": "admin",
        }, follow_redirects=True, headers={"content-type": "application/x-www-form-urlencoded"})
        assert login_response.status_code == 200
        logout_response = c.post('/Logout', follow_redirects=True)
        assert logout_response.status_code == 200


def test_logout():
    """ This test really shouldn't work as a new context is being used and to log out you have to be logged in.  """
    with app.test_client() as c:
        logout_response = c.post('/Logout', follow_redirects=True)
        assert logout_response.status_code == 200
