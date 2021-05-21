from sunc.settings import (VERSION, APP_NAME)

import urllib.error
import urllib.request
import urllib.parse
import json


class Response:
    """
    Class ressponsible for evaluating the responses of the request, you can retrieve it as content, or as JSON by now.
    """
    def __init__(self, response, decode_format=None):
        self.response = response
        self.status_code = response.code
        self.decode_format = decode_format if decode_format else 'utf-8'
    
    @property
    def content(self):
        return self.response.read().decode(self.decode_format)

    @property
    def json(self):
        response_json_string = self.response.read().decode(self.decode_format)
        data = json.loads(response_json_string)
        return data


class Request:
    """
    Class responsible for making HTTP requests in pure python, without the need of external packages
    """
    def __init__(self, headers={}):
        self.__headers = {
            'User-Agent': '%s/%s' % (APP_NAME, VERSION)
        }
        self.__headers.update(headers)

    def __prepare_parameters(self, params):
        url_parameters = urllib.parse.urlencode(params)
        return url_parameters

    def __prepare_data(self, data, json_data):
        if json:
            dumped_json = json.dumps(json_data)
            data = dumped_json.encode('utf-8')
        else:
            data = urllib.parse.urlencode(data)
            data = data.encode('ascii')
        return data

    def __prepare_url(self, url, params):
        prepared_parameters = self.__prepare_parameters(params)
        return '%s?%s' % (url, prepared_parameters) if prepared_parameters != '' else url

    def __prepare_headers(self, headers, is_json):
        """
        Prepares the headers for the request, this append obligatory headers like when the user sends a JSON and also formats.

        Args:
            headers (dict[str, str]): A dict of strings as keys and strings as values
            is_json (bool): If the request is a json this must be set to True, otherwise False

        Returns:
            dict[str, str]: Returns a newly formated dict of headers
        """
        headers.update(self.__headers)
        if is_json:
            headers['Content-Type'] = 'application/json; charset=utf-8'

        return headers

    def request(self, method, url, data={}, json={}, headers={}, params={}):
        is_json = True if json else False

        prepared_data = self.__prepare_data(data, json)
        prepared_header = self.__prepare_headers(headers, is_json)
        prepared_url = self.__prepare_url(url, params)

        request = urllib.request.Request(url=prepared_url, data=prepared_data, headers=prepared_header)
        request.get_method = lambda: method.upper()
        try:
            request_response = urllib.request.urlopen(request)
            response = Response(
                response=request_response
            )
        except urllib.error.HTTPError as httpe:
            response = Response(
                response=httpe
            )
        
        return response

    def get(self, url, params={}, **kwargs):
        return self.request('GET',url, params=params, **kwargs)

    def post(self, url, data={}, json={}, **kwargs):
        return self.request('POST', url, data=data, json=json, **kwargs)
    
    def patch(self, url, data={}, json={}, **kwargs):
        return self.request('PATCH', url, data=data, json=json, **kwargs)