from sbr_ui.utilities.helpers import compose, convert_band, base_64_encode, format_children, convert_bands
from sbr_ui.utilities.helpers import  sic, sic07, trading_status, legal_status, employment_band, turnover_band


class TestHelperMethods(object):
    def test_compose(self):
        add_one = lambda x: x + 1
        multiply_by_five = lambda x: x * 5

        add_one_then_multiply = compose(add_one, multiply_by_five)

        assert add_one_then_multiply(1) == 10

    def test_convert_band(self):
        original = "12345"
        converted_value = "98765"
        assert convert_band({"sic07": original}, "sic07", "sic code", {original:converted_value}) == \
               {"sic07": f"{original} - {converted_value}"}

    def test_convert_band_not_found_msg(self):
        original = "12345"
        converted_value = "98765"
        not_found_message = "sic code"
        assert convert_band({"sic07": original}, "sic07", not_found_message, {"0": converted_value}) == \
               {"sic07": f"{original} - No {not_found_message} could be found"}

    def test_convert_band_invalid_key(self):
        original = "12345"
        converted_value = "98765"
        assert convert_band({"sic07": original}, "sic0789", "sic code", {original: converted_value}) == \
               {"sic07": original}

    def test_base_64_encoding(self):
        assert base_64_encode("abcd") == b'YWJjZA=='

    def test_format_children_single(self):
        assert format_children({"2": "LEU","3": "LOU","4": "CH","5": "PAYE","6": "VAT"}) == {
            "LEU": ["2"],
            "LOU": ["3"],
            "CH": ["4"],
            "PAYE": ["5"],
            "VAT": ["6"]
        }

    def test_format_children_multiple(self):
        assert format_children({"2": "LEU", "3": "LEU", "4": "LEU"}) == {"LEU": ["2","3","4"]}

    def test_sic_conversion(self):
        assert sic({"name": "John", "industryCode": "33150"}) == \
               {"name": "John", "industryCode": "33150 - Repair and maintenance of ships and boats"}\

    def test_sic_not_found_conversion(self):
        assert sic({"name": "John", "industryCode": "999999"}) == \
               {"name": "John", "industryCode": "999999 - No industry code description could be found"}

    def test_sic_07_conversion(self):
        assert sic07({"sic07": "33150"}) == {"sic07": "33150 - Repair and maintenance of ships and boats"}

    def test_sic_07_not_found_conversion(self):
        assert sic07({"sic07": "3315099"}) == {"sic07": "3315099 - No industry code description could be found"}

    def test_trading_status_conversion(self):
        assert trading_status({"tradingStatus": "A"}) == {"tradingStatus": "A - Active"}

    def test_trading_status_not_found_conversion(self):
        assert trading_status({"tradingStatus": "Z"}) == {"tradingStatus": "Z - No trading status could be found"}

    def test_legal_status_conversion(self):
        assert legal_status({"legalStatus": "1"}) == {"legalStatus": "1 - Company"}

    def test_legal_status_not_found_conversion(self):
        assert legal_status({"legalStatus": "100"}) == {"legalStatus": "100 - No legal status could be found"}

    def test_employment_band_conversion(self):
        assert employment_band({"employmentBands": "A"}) == {"employmentBands": "A - 0"}

    def test_employment_band_not_found_conversion(self):
        assert employment_band({"employmentBands": "Z"}) == {"employmentBands": "Z - No employment band could be found"}

    def test_turnover_band_conversion(self):
        assert turnover_band({"turnover": "A"}) == {"turnover": "A - 0-99"}

    def test_turnover_band_not_found_conversion(self):
        assert turnover_band({"turnover": "Z"}) == {"turnover": "Z - No turnover band could be found"}

    def test_convert_bands_composition(self):
        assert convert_bands({
            "industryCode": "33150","sic07": "33150","tradingStatus": "A","legalStatus": "1",
            "employmentBands": "A","turnover": "A"
        }) == {
            "industryCode": "33150 - Repair and maintenance of ships and boats",
            "sic07": "33150 - Repair and maintenance of ships and boats","tradingStatus": "A - Active",
            "legalStatus": "1 - Company","employmentBands": "A - 0","turnover": "A - 0-99"
        }