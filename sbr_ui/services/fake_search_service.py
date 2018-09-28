import logging
import requests
from structlog import wrap_logger


logger = wrap_logger(logging.getLogger(__name__))


class FakeSearchService:
    Unit = dict

    @staticmethod
    def search_by_id(unit_id: str) -> Unit:
        logger.info("Search by unit id", unit_id=unit_id)

        matches = list(filter(lambda x: x["id"] == unit_id, units))
        if len(matches) > 0:
            return matches[0].copy()
        else:
            raise requests.exceptions.HTTPError("Not Found", 404)

    @staticmethod
    def get_unit_by_id_type_period(unit_id: str, unit_type: str, period: str) -> Unit:
        logger.info("Search by unit id, unit type and period", unit_id=unit_id, unit_type=unit_type, period=period)
        matches = list(filter(lambda x:
                              x["id"] == unit_id and
                              x["period"] == period and
                              x["unitType"] == unit_type, units))

        if len(matches) > 0:
            return matches[0].copy()
        else:
            raise requests.exceptions.HTTPError("Not Found", 404)


units = [{
    "id": "1",
    "unitType": "ENT",
    "period": "201810",
    "children": {
        "2": "LEU",
        "3": "LU",
        "4": "CH",
        "5": "PAYE",
        "6": "VAT"
    },
    "vars": {
        "ern": "918237891237",
        "entref": "879372942",
        "name": "Tesco",
        "tradingStyle": "3",
        "sic07": "10000",
        "legalStatus": "1",
        "employees": "68",
        "jobs": "1038",
        "turnover": "8362",
        "prn": "0387",
        "workingProprietors": "8",
        "employment": "334",
        "region": "Gwent",
        "address": {
            "line1": '6 Big House',
            "line2": 'Long Street',
            "line3": 'Newport',
            "line4": 'South Wales',
            "line5": 'Wales',
            "postcode": 'NP20 ABC',
        },
    }
},{
    "id": "2",
    "unitType": "LEU",
    "period": "201810",
    "parents": {
        "ENT": "1"
    },
    "children": {
        "4": "CH",
        "5": "PAYE",
        "6": "VAT"
    },
    "vars": {
        "ubrn": "871827912739123",
        "name": "Asda Stores",
        "legalStatus": "1",
        "tradingStatus": "1",
        "tradingStyle": "1",
        "sic07": "10000",
        "turnover": "3",
        "payeJobs": "4",
        "birthDate": "2018",
        "deathDate": "2019",
        "deathCode": "12",
        "crn": "333",
        "uprn": "444",
        "address": {
            "line1": '22 Smith Street',
            "line2": 'Cardiff Road',
            "line3": 'Cwmbran',
            "line4": 'South Wales',
            "line5": 'Wales',
            "postcode": 'NP20 DEF',
        },
    }
},{
    "id": "3",
    "unitType": "LU",
    "period": "201810",
    "parents": {
        "ENT": "1"
    },
    "vars": {
        "name": "Morrisons",
        "lurn": "3",
        "luref": "82397243",
        "enterprise": { "ern": "1", "entref": "871823979123" },
        "reportingUnit": { "rurn": "234234234", "luref": "83749272479" },
        "tradingStyle": "2",
        "sic07": "10000",
        "employees": "4",
        "employment": "8",
        "prn": "0.22",
        "region": "Wales",
        "address": {
            "line1": '56 Six Street',
            "line2": 'Bristol Road',
            "line3": 'Chepstow',
            "line4": 'South Wales',
            "line5": 'Wales',
            "postcode": 'NP20 QWE',
        }
    }
},{
    "id": "4",
    "unitType": "CH",
    "period": "201810",
    "parents": {
        "ENT": "1",
        "LEU": "2"
    },
    "vars": {
        "businessName": "Waitrose",
        "tradingStatus": "2",
        "legalStatus": "7",
        "postCode": "NP20 QQQ",
        "industryCode": "4",
        "employmentBands": "8",
        "turnover": "2"
    }
},{
    "id": "5",
    "unitType": "PAYE",
    "period": "201810",
    "parents": {
        "ENT": "1",
        "LEU": "2"
    },
    "vars": {
        "businessName": "Booths",
        "tradingStatus": "4",
        "legalStatus": "2",
        "postCode": "NP20 PPP",
        "industryCode": "1",
        "employmentBands": "7",
        "turnover": "3"
    }
},{
    "id": "6",
    "unitType": "VAT",
    "period": "201810",
    "parents": {
        "ENT": "1",
        "LEU": "2"
    },
    "vars": {
        "businessName": "Aldi",
        "tradingStatus": "5",
        "legalStatus": "8",
        "postCode": "NP20 ZZZ",
        "industryCode": "4",
        "employmentBands": "6",
        "turnover": "7"
    }
}]
