import requests
from endpoints.create_url_endpoint import CreateUrlEndpoint
import pytest

def test_create_short_url(create_url_endpoint):
    site_url = 'https://www.discovery.com//shark-week/se-schedule-2023-pictures'
     
    create_url_endpoint.create_short_url_for_url(site_url)
    
    create_url_endpoint.check_response_status_is_ok()
    create_url_endpoint.check_long_url_same_as_sent()
    create_url_endpoint.check_tiny_url_is_not_empty()



def test_customer_short_url(create_url_endpoint):
    site_url = 'https://www.discovery.com//shark-week/se-schedule-2023-pictures'
    code = '123pkfjklc'

    create_url_endpoint.create_short_url_for_url(site_url, code)
    create_url_endpoint.check_response_status_is_ok()
    create_url_endpoint.check_long_url_same_as_sent()
    create_url_endpoint.check_short_code_same_as_sent()