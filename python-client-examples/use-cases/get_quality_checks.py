from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.QualityChecksApi(swagger_client.ApiClient(configuration))

data_store = 0

try:
    # Get Quality Checks
    api_response = api_instance.get_quality_checks(data_store=data_store)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityChecksApi->get_quality_checks: %s\n" % e)