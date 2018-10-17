import pytest

from sbr_ui.services.fake_search_service import FakeSearchService
from test_data import enterprise, legal_unit
from tests.constants import ERN, UBRN, LEGAL_UNIT


class TestFakeSearchService(object):

    @pytest.fixture
    def search(self):
        return FakeSearchService

    def test_search_by_id(self, search):
        unit_result = search.search_by_id(ERN)
        assert unit_result == enterprise

    def test_get_unit_by_id_type_period(self, search):
        target_period = "201810"
        unit_result = search.get_unit_by_id_type_period(UBRN, LEGAL_UNIT, target_period)
        assert unit_result == legal_unit
