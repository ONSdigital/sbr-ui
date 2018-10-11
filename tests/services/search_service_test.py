import pytest
import responses

from sbr_ui import create_application
from sbr_ui.models.exceptions import ApiError
from test_data import enterprise, legal_unit, reporting_unit, local_unit, value_added_tax, pay_as_you_earn, company_house
from sbr_ui.services.search_service import SearchService
from tests.constants import ENTREF, UBRN, RURN, LURN, VATREF, PAYEREF, CRN


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
    url = f'http://localhost:9000/v1/search/{ENTREF}'
    responses.add(responses.GET, url, json=enterprise, status=200)
    with app.app_context():
        json = search.search_by_id(ENTREF)
    assert json == enterprise


@responses.activate
def test_search_by_id_leu(search, app):
    url = f'http://localhost:9000/v1/search/{UBRN}'
    responses.add(responses.GET, url, json=legal_unit, status=200)
    with app.app_context():
        json = search.search_by_id(UBRN)
    assert json == legal_unit


@responses.activate
def test_search_by_id_lou(search, app):
    url = f'http://localhost:9000/v1/search/{LURN}'
    responses.add(responses.GET, url, json=local_unit, status=200)
    with app.app_context():
        json = search.search_by_id(LURN)
    assert json == local_unit


@responses.activate
def test_search_by_id_reu(search, app):
    url = f'http://localhost:9000/v1/search/{RURN}'
    responses.add(responses.GET, url, json=reporting_unit, status=200)
    with app.app_context():
        json = search.search_by_id(RURN)
    assert json == reporting_unit


@responses.activate
def test_search_by_id_vat(search, app):
    url = f'http://localhost:9000/v1/search/{VATREF}'
    responses.add(responses.GET, url, json=value_added_tax, status=200)
    with app.app_context():
        json = search.search_by_id(VATREF)
    assert json == value_added_tax


@responses.activate
def test_search_by_id_paye(search, app):
    url = f'http://localhost:9000/v1/search/{PAYEREF}'
    responses.add(responses.GET, url, json=pay_as_you_earn, status=200)
    with app.app_context():
        json = search.search_by_id(PAYEREF)
    assert json == pay_as_you_earn


@responses.activate
def test_search_by_id_ch(search, app):
    url = f'http://localhost:9000/v1/search/{CRN}'
    responses.add(responses.GET, url, json=company_house, status=200)
    with app.app_context():
        json = search.search_by_id(CRN)
    assert json == company_house


@responses.activate
def test_search_by_id_500(search, app):
    url = f'http://localhost:9000/v1/search/{PAYEREF}'
    responses.add(responses.GET, url, status=500)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            search.search_by_id(PAYEREF)
    assert err.value.status_code == 500
    assert err.value.url == url


@responses.activate
def test_search_by_id_404(search, app):
    url = f'http://localhost:9000/v1/search/{PAYEREF}'
    responses.add(responses.GET, url, status=404)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            search.search_by_id(PAYEREF)
    assert err.value.status_code == 404
    assert err.value.url == url


@responses.activate
def test_search_by_id_type_period_ent(search, app):
    target_unit_type = "ENT"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/ents/{ENTREF}'
    responses.add(responses.GET, url, json=enterprise, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(ENTREF, target_unit_type, target_period)
    assert json == enterprise


@responses.activate
def test_search_by_id_type_period_leu(search, app):
    target_unit_type = "LEU"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/leus/{UBRN}'
    responses.add(responses.GET, url, json=legal_unit, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(UBRN, target_unit_type, target_period)
    assert json == legal_unit


@responses.activate
def test_search_by_id_type_period_lou(search, app):
    target_unit_type = "LOU"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/lous/{LURN}'
    responses.add(responses.GET, url, json=local_unit, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(LURN, target_unit_type, target_period)
    assert json == local_unit


@responses.activate
def test_search_by_id_type_period_reu(search, app):
    target_unit_type = "REU"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/reus/{RURN}'
    responses.add(responses.GET, url, json=reporting_unit, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(RURN, target_unit_type, target_period)
    assert json == reporting_unit


@responses.activate
def test_search_by_id_type_period_vat(search, app):
    target_unit_type = "VAT"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/vats/{VATREF}'
    responses.add(responses.GET, url, json=value_added_tax, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(VATREF, target_unit_type, target_period)
    assert json == value_added_tax


@responses.activate
def test_search_by_id_type_period_paye(search, app):
    target_unit_type = "PAYE"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/payes/{PAYEREF}'
    responses.add(responses.GET, url, json=pay_as_you_earn, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(PAYEREF, target_unit_type, target_period)
    assert json == pay_as_you_earn


@responses.activate
def test_search_by_id_type_period_ch(search, app):
    target_unit_type = "CH"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/crns/{CRN}'
    responses.add(responses.GET, url, json=company_house, status=200)
    with app.app_context():
        json = search.get_unit_by_id_type_period(CRN, target_unit_type, target_period)
    assert json == company_house


@responses.activate
def test_search_by_id_type_period_500(search, app):
    target_unit_type = "CH"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/crns/{CRN}'
    responses.add(responses.GET, url, status=500)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            search.get_unit_by_id_type_period(CRN, target_unit_type, target_period)
    assert err.value.status_code == 500
    assert err.value.url == url


@responses.activate
def test_search_by_id_type_period_404(search, app):
    target_unit_type = "CH"
    target_period = "201810"
    url = f'http://localhost:9000/v1/periods/{target_period}/crns/{CRN}'
    responses.add(responses.GET, url, status=404)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            search.get_unit_by_id_type_period(CRN, target_unit_type, target_period)
    assert err.value.status_code == 404
    assert err.value.url == url

