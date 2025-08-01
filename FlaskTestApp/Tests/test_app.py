import pytest

from FlaskTestApp.API.ApplicationAPI import URLHandler
from FlaskTestApp.Data.data_for_test import data_for_reversed_strings, data_for_invalid_inputs
from FlaskTestApp.Util.Logger import getLogger


@pytest.mark.usefixtures("setup")
class Test_application(URLHandler):
    # Initialize the logger at the class level
    logger = getLogger()

    tmp_input_string = None

    # Test reverse API with valid input
    @pytest.mark.parametrize("data", data_for_reversed_strings())
    def test_reverse_valid_input(self, data):
        url = self.build_url()
        input_string = data["input_string"]
        expected_result = data["expected_result"]

        response = self.reverse_request(url, input_string)
        data_response = response.json()
        self.logger.info("Response status code:" + str(response.status_code))

        assert response.status_code == 200
        assert data_response["result"] == expected_result
        Test_application.tmp_input_string = data["input_string"]

    # Test restore API with valid input
    def test_restore_valid_input(self):
        url = self.build_url()
        expected_result = Test_application.tmp_input_string

        response = self.restore_request(url)
        data_response = response.json()
        self.logger.info("Response status code:" + str(response.status_code))

        assert response.status_code == 200
        assert data_response["Source"] == expected_result

    # Test reverse with empty input
    def test_reverse_empty_input(self):
        url = self.build_url()

        response = self.reverse_request(url, "")
        data_response = response.json()
        self.logger.info("Response status code:" + str(response.status_code))

        assert response.status_code == 200
        assert data_response["result"] == ""

    # Test restore with empty input
    def test_restore_empty_input(self):
        url = self.build_url()

        response = self.restore_request(url)
        data_response = response.json()
        self.logger.info("Response status code:" + str(response.status_code))

        assert response.status_code == 200
        assert data_response["Source"] == ""

    # Test API with invalid input
    @pytest.mark.parametrize("invalid_input", data_for_invalid_inputs())
    def test_restore_invalid_input(self, invalid_input):
        url = self.build_url()
        url_invalid_endpoint = url + invalid_input['input']

        response = self.restore_request(url_invalid_endpoint)
        self.logger.info("Response status code:" + str(response.status_code))
        assert response.status_code == 404

    def test_push(self):
        print("test push")
