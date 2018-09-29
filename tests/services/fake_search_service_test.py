import pytest

from sbr_ui.services.fake_search_service import FakeSearchService
from test_data import units, enterprise, legal_unit


class TestFakeSearchService(object):

    @pytest.fixture
    def search(self):
        return FakeSearchService(units)

    def test_search_by_id(self, search):
        target_id = "1"
        unit_result = search.search_by_id(target_id)
        assert unit_result == enterprise

    def test_get_unit_by_id_type_period(self, search):
        target_id = "2"
        target_unit_type = "LEU"
        target_period = "201810"
        unit_result = search.get_unit_by_id_type_period(target_id, target_unit_type, target_period)
        assert unit_result == legal_unit
