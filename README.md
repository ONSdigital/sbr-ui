# sbr-ui

[![phase](https://img.shields.io/badge/phase-BETA-orange.svg)](https://img.shields.io/badge/phase-BETA-orange.svg) [![license](https://img.shields.io/github/license/mashape/apistatus.svg)](./LICENSE)

A proof of concept of the Statistical Business Register User Interface using Flask.

Previous repository: https://github.com/ONSdigital/sbr-ui

### Table of Contents
**[1. Environment Setup](#environment-setup)**<br>
**[2. Running Instructions](#running-instructions)**<br>
**[3. Testing](#testing)**<br>
**[4. Dependencies](#dependencies)**<br>
**[5. Troubleshooting](#troubleshooting)**<br>
**[6. Contributing](#contributing)**<br>
**[7. License](#license)**<br>

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

## Testing

To run the `pytest` tests, use the following command:

```shell
ENVIRONMENT=TEST pytest --ignore=tests/selenium
```

To run the Selenium tests, use the following command:

```shell
pytest tests/selenium/
```

For the Selenium user interface tests to work, you will need to do the following:
- install Firefox
- install the `geckodriver` used by Selenium: `brew install geckodriver`
- run `sbr-ui`, making sure to pass in `USE_FAKE_DATA=True`

## Dependencies

* [flask-login](http://flask-login.readthedocs.io/en/latest/)
* [flask-session](http://flask-session.readthedocs.io/en/latest/)
* [flask-restful](http://flask-restful.readthedocs.io/en/latest/)

## Troubleshooting

If your updates to static files aren't registering, reset the cache (shift + press refresh in Chrome).

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for details.

## License

Copyright ©‎ 2018, Office for National Statistics (https://www.ons.gov.uk)

Released under MIT license, see [LICENSE](./LICENSE) for details.