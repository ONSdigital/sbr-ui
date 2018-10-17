# sbr-ui

[![phase](https://img.shields.io/badge/phase-BETA-orange.svg)](https://img.shields.io/badge/phase-BETA-orange.svg) [![license](https://img.shields.io/github/license/mashape/apistatus.svg)](./LICENSE)

A proof of concept of the Statistical Business Register User Interface using Flask.

Previous repository: https://github.com/ONSdigital/sbr-react-ui

### Table of Contents
**[1. Environment Setup](#environment-setup)**<br>
**[2. Running Instructions](#running-instructions)**<br>
**[3. Environment Variables](#environment-variables)**<br>
**[4. Testing](#testing)**<br>
**[5. Dependencies](#dependencies)**<br>
**[6. Troubleshooting](#troubleshooting)**<br>
**[7. Contributing](#contributing)**<br>
**[8. License](#license)**<br>

## Environment Setup

Firstly, install Python 3:

```shell
brew install python
```

Create a virtual environment (from inside the cloned repository):

```shell
python3 -m venv venv
```

## Running Instructions

Activate the virtual environment:

```shell
source venv/bin/activate
```

Install dependencies from the `requirements.txt` file:

```shell
pip install -r requirements.txt
```

Run the server in development mode, with hot-reloading:

```shell
FLASK_APP=run.py FLASK_DEBUG=1 ENVIRONMENT=DEV python3 -m flask run
```

Note: `USE_FAKE_DATA=True` can be passed in to allow the application to run without `sbr-api`. The test data is held [here](./sbr_ui/utilities/units.py).

The user interface can be accessed on http://localhost:5000.

## Environment Variables

| Environment Variable | Default Value              |
|----------------------|----------------------------|
| ENVIRONMENT          | DEV                        |
| USE_FAKE_DATA        | False                      |
| LOG_LEVEL            | INFO                       |
| API_TIMEOUT          | 2 (seconds)                |
| AUTH_TIMEOUT         | 2 (seconds)                |
| AUTH_URL             | http://localhost:3002/auth |
| API_URL              | http://localhost:9000      |
| SECRET_KEY           | change_me                  |

The server will not start unless you have set `ENVIRONMENT` to one of `DEV`/`TEST`/`PROD`.

In `PROD` mode, the server will only start if you have set `AUTH_URL`, `API_URL` and `SECRET_KEY`.

## Testing

### Server Tests

To run the `pytest` tests, use the following command:

```shell
ENVIRONMENT=TEST pytest --ignore=tests/selenium
```

### User Interface Selenium Tests

To run the Selenium tests, use the following command:

```shell
pytest tests/selenium/
```

For the Selenium user interface tests to work, you will need to do the following:
- Install Firefox
- Install the `geckodriver` used by Selenium: `brew install geckodriver`
- Run `sbr-ui`, making sure to pass in `USE_FAKE_DATA=True`

If you want to run the Selenium tests in headless mode, pass in `SELENIUM_HEADLESS=True`.

### Test Coverage

To generate test coverage using `pytest-cov`, use the following command:

```shell
ENVIRONMENT=TEST pytest --cov-report html --cov=sbr_ui --ignore=tests/selenium
```

Coverage reports are saved to `./htmlcov`. Open `./htmlcov/index.html` in a browser to inspect the results.

## Dependencies

* [flask](http://flask.pocoo.org/)
* [flask-login](http://flask-login.readthedocs.io/en/latest/)
* [flask-session](http://flask-session.readthedocs.io/en/latest/)
* [requests](http://docs.python-requests.org/en/master/)
* [structlog](https://pypi.org/project/structlog/)
* [colorama](https://pypi.org/project/colorama/)
* [pytest](https://docs.pytest.org/en/latest/)
* [selenium](https://selenium-python.readthedocs.io/)
* [pytest-cov](https://pypi.org/project/pytest-cov/)

## Troubleshooting

If your updates to static files aren't registering, reset the cache (shift + press refresh in Chrome).

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for details.

## License

Copyright ©‎ 2018, Office for National Statistics (https://www.ons.gov.uk)

Released under MIT license, see [LICENSE](./LICENSE) for details.