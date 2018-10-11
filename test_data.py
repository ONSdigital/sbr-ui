enterprise = {
    "id": "1",
    "unitType": "ENT",
    "period": "201810",
    "children": {
        "2": "LEU",
        "3": "LOU",
        "4": "CH",
        "5": "PAYE",
        "6": "VAT"
    },
    "vars": {
        "ern": "1",
        "entref": "879372942",
        "name": "Tesco",
        "tradingStyle": "3",
        "sic07": "43120",
        "legalStatus": "1",
        "employees": "68",
        "jobs": "1038",
        "turnover": "A",
        "prn": "0387",
        "workingProprietors": "8",
        "employment": "A",
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
}

legal_unit = {
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
        "ubrn": "2",
        "name": "Asda Stores",
        "legalStatus": "7",
        "tradingStatus": "A",
        "tradingStyle": "1",
        "sic07": "39000",
        "turnover": "F",
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
}

local_unit = {
    "id": "3",
    "unitType": "LOU",
    "period": "201810",
    "parents": {
        "ENT": "1"
    },
    "vars": {
        "name": "Morrisons",
        "lurn": "3",
        "luref": "82397243",
        "enterprise": { "ern": "1", "entref": "871823979123" },
        "reportingUnit": { "rurn": "234234234", "ruref": "83749272479" },
        "tradingStyle": "2",
        "sic07": "35230",
        "employees": "4",
        "employment": "D",
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
}

company_house = {
    "id": "4",
    "unitType": "CH",
    "period": "201810",
    "parents": {
        "ENT": "1",
        "LEU": "2"
    },
    "vars": {
        "businessName": "Waitrose",
        "tradingStatus": "D",
        "legalStatus": "5",
        "postCode": "NP20 QQQ",
        "industryCode": "32409",
        "employmentBands": "F",
        "turnover": "C"
    }
}

pay_as_you_earn = {
    "id": "5",
    "unitType": "PAYE",
    "period": "201810",
    "parents": {
        "ENT": "1",
        "LEU": "2"
    },
    "vars": {
        "businessName": "Booths",
        "tradingStatus": "C",
        "legalStatus": "2",
        "postCode": "NP20 PPP",
        "industryCode": "02200",
        "employmentBands": "B",
        "turnover": "E"
    }
}

value_added_tax = {
    "id": "6",
    "unitType": "VAT",
    "period": "201810",
    "parents": {
        "ENT": "1",
        "LEU": "2"
    },
    "vars": {
        "businessName": "Aldi",
        "tradingStatus": "A",
        "legalStatus": "8",
        "postCode": "NP20 ZZZ",
        "industryCode": "01160",
        "employmentBands": "G",
        "turnover": "A"
    }
}

units = [enterprise, legal_unit, local_unit, company_house, pay_as_you_earn, value_added_tax]