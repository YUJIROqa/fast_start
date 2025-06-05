import pytest
from endpoints.create_url_endpoint import CreateUrlEndpoint

@pytest.fixture
def create_url_endpoint():
    return CreateUrlEndpoint()

