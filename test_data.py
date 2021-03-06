enterprise = {
    "id": "1234567890",
    "unitType": "ENT",
    "period": "201810",
    "children": {
        "7584930284759231": "LEU",
        "849204991": "LOU",
        "78391432987": "REU",
        "44599148": "CH",
        "736FB28947": "PAYE",
        "663828891038": "VAT"
    },
    "vars": {
        "ern": "1234567890",
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
        "imputed": {
            "employees": "4",
            "turnover": "2"
        }
    }
}

legal_unit = {
    "id": "7584930284759231",
    "unitType": "LEU",
    "period": "201810",
    "parents": {
        "ENT": "1234567890"
    },
    "children": {
        "44599148": "CH",
        "736FB28947": "PAYE",
        "663828891038": "VAT"
    },
    "vars": {
        "ubrn": "7584930284759231",
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
        }
    }
}

local_unit = {
    "id": "849204991",
    "unitType": "LOU",
    "period": "201810",
    "parents": {
        "ENT": "1234567890"
    },
    "vars": {
        "name": "Morrisons",
        "lurn": "849204991",
        "luref": "82397243",
        "enterprise": { "ern": "1234567890", "entref": "871823979123" },
        "reportingUnit": { "rurn": "78391432987", "ruref": "83749272479" },
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
    "id": "44599148",
    "unitType": "CH",
    "period": "201810",
    "parents": {
        "ENT": "1234567890",
        "LEU": "7584930284759231"
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
    "id": "736FB28947",
    "unitType": "PAYE",
    "period": "201810",
    "parents": {
        "ENT": "1234567890",
        "LEU": "7584930284759231"
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
    "id": "663828891038",
    "unitType": "VAT",
    "period": "201810",
    "parents": {
        "ENT": "1234567890",
        "LEU": "7584930284759231"
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

reporting_unit = {
    "id": "78391432987",
    "unitType": "REU",
    "period": "201810",
    "parents": {
        "ENT": "1234567890"
    },
    "vars": {
        "rurn": "78391432987",
        "ruref": "123837",
        "ern": "1234567890",
        "entref": "334112",
        "name": "Booths",
        "tradingStyle": "Booths Limited",
        "legalStatus": "1",
        "sic07": "60000",
        "employees": "5",
        "employment": "9",
        "turnover": "839",
        "prn": "0.016587362",
        "region": "South",
        "address": {
            "line1": "27 Titchfield Street",
            "line2": "Southampton Road",
            "line3": "London",
            "line4": "Greater London",
            "line5": "England",
            "postcode": "ABCD EFG"
        }
    }
}

units = [enterprise, legal_unit, local_unit, reporting_unit, company_house, pay_as_you_earn, value_added_tax]