import requests

from FlaskTestApp.Util.Read_INI_File import read_config_ini


class URLHandler:
    def build_url(self):
        server_host = read_config_ini()['Server']['host']
        server_port = read_config_ini()['Port']['Port']
        url = f"http://{server_host}:{server_port}"
        return url

    def reverse_request(self, url, input_string):
        response = requests.get(url + "/reverse", params={"in": input_string})
        return response

    def restore_request(self, url):
        response = requests.get(url + "/restore")
        return response