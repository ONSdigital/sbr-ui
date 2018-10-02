import pytest
import responses

from sbr_ui import create_application
from sbr_ui.models.exceptions import ApiError
from test_data import enterprise, legal_unit, local_unit, value_added_tax, pay_as_you_earn, company_house
from sbr_ui.services.search_service import SearchService


@pytest.fixture
def search():
    return SearchService

@pytest.fixture
def app():
    app = create_application()
    app.config.update(ENVIRONMENT='TEST')
    return app

@responses.activate
def test_search_by_id_ent(search, app):
    target_id = "1"
    url = f'http://localhost:9000/v1/search/{target_id}'
    responses.add(responses.GET, url, json=enterprise, status=200)
    with app.app_context():
        json = search.search_by_id(target_id)
    assert json == enterprise

@responses.activate
def test_search_by_id_leu(search, app):
    target_id = "2"
    url = f'http://localhost:9000/v1/search/{target_id}'
    responses.add(responses.GET, url, json=legal_unit, status=200)
    with app.app_context():
        json = search.search_by_id(target_id)
    assert json == legal_unit

@responses.activate
def test_search_by_id_lu(search, app):
    target_id = "3"
    url = f'http://localhost:9000/v1/search/{target_id}'
    responses.add(responses.GET, url, json=local_unit, status=200)
    with app.app_context():
        json = search.search_by_id(target_id)
    assert json == local_unit

@responses.activate
def test_search_by_id_vat(search, app):
    target_id = "4"
    url = f'http://localhost:9000/v1/search/{target_id}'
    responses.add(responses.GET, url, json=value_added_tax, status=200)
    with app.app_context():
        json = search.search_by_id(target_id)
    assert json == value_added_tax

@responses.activate
def test_search_by_id_paye(search, app):
    target_id = "5"
    url = f'http://localhost:9000/v1/search/{target_id}'
    responses.add(responses.GET, url, json=pay_as_you_earn, status=200)
    with app.app_context():
        json = search.search_by_id(target_id)
    assert json == pay_as_you_earn

@responses.activate
def test_search_by_id_ch(search, app):
    target_id = "6"
    url = f'http://localhost:9000/v1/search/{target_id}'
    responses.add(responses.GET, url, json=company_house, status=200)
    with app.app_context():
        json = search.search_by_id(target_id)
    assert json == company_house

@responses.activate
def test_search_by_id_500(search, app):
    target_id = "6"
    url = f'http://localhost:9000/v1/search/{target_id}'
    responses.add(responses.GET, url, status=500)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            search.search_by_id(target_id)
    assert err.value.status_code == 500
    assert err.value.url == url

@responses.activate
def test_search_by_id_404(search, app):
    target_id = "6"
    url = f'http://localhost:9000/v1/search/{target_id}'
    responses.add(responses.GET, url, status=404)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            search.search_by_id(target_id)
    assert err.value.status_code == 404
    assert err.value.url == url

@responses.activate
def test_search_by_id_type_period_ent(search, app):
    target_id = "1"
    target_unit_type = "ENT"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/ents/{target_id}'
    responses.add(responses.GET, url, json=enterprise, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
    assert json == enterprise

@responses.activate
def test_search_by_id_type_period_leu(search, app):
    target_id = "2"
    target_unit_type = "LEU"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/leus/{target_id}'
    responses.add(responses.GET, url, json=legal_unit, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
    assert json == legal_unit

@responses.activate
def test_search_by_id_type_period_lu(search, app):
    target_id = "3"
    target_unit_type = "LU"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/lous/{target_id}'
    responses.add(responses.GET, url, json=local_unit, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
    assert json == local_unit

@responses.activate
def test_search_by_id_type_period_vat(search, app):
    target_id = "4"
    target_unit_type = "VAT"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/vats/{target_id}'
    responses.add(responses.GET, url, json=value_added_tax, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
    assert json == value_added_tax

@responses.activate
def test_search_by_id_type_period_paye(search, app):
    target_id = "5"
    target_unit_type = "PAYE"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/payes/{target_id}'
    responses.add(responses.GET, url, json=pay_as_you_earn, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
    assert json == pay_as_you_earn

@responses.activate
def test_search_by_id_type_period_ch(search, app):
    target_id = "6"
    target_unit_type = "CH"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/crns/{target_id}'
    responses.add(responses.GET, url, json=company_house, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
    assert json == company_house

@responses.activate
def test_search_by_id_type_period_500(search, app):
    target_id = "6"
    target_unit_type = "CH"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/crns/{target_id}'
    responses.add(responses.GET, url, status=500)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
    assert err.value.status_code == 500
    assert err.value.url == url

@responses.activate
def test_search_by_id_type_period_404(search, app):
    target_id = "6"
    target_unit_type = "CH"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/crns/{target_id}'
    responses.add(responses.GET, url, status=404)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
    assert err.value.status_code == 404
    assert err.value.url == url

