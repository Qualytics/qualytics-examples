from __future__ import print_function
import sys
import os
from pprint import pprint

# Add the parent directory to the path so we can import swagger_client
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import swagger_client

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
datastore_id = 1734

try:
    # Get Containers
    api_response = api_instance.get_containers(datastore = datastore_id)
    pprint(api_response)
except swagger_client.ApiException as e:
    print("Exception when calling ContainersApi->get_containers: %s\n" % e)