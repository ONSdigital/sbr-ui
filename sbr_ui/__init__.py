from sbr_ui.create_app import create_application
from sbr_ui.services.fake_search_service import FakeSearchService
from sbr_ui.services.search_service import SearchService

app = create_application()


def get_search_service(config):
    """ TODO: get the service once at runtime, not on every search """
    if config['USE_FAKE_DATA']:
        return FakeSearchService
    return SearchService

import sbr_ui.routes
