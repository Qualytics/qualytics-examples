from __future__ import print_function
import time
import swagger_client
import os
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.DataStoresApi(swagger_client.ApiClient(configuration))

try:
    # Create Data Store
    api_response = api_instance.get_data_stores()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_data_stores: %s\n" % e)
