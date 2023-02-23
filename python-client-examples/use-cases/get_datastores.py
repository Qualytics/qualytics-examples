from __future__ import print_function
import time
import swagger_client
import os
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.DatastoresApi(swagger_client.ApiClient(configuration))

try:
    # Create Datastore
    api_response = api_instance.get_datastores()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatastoresApi->get_datastores: %s\n" % e)
