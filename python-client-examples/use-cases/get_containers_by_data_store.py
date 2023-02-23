from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
datastore_id = 0

try:
    # Get Containers
    api_response = api_instance.get_containers(datastore = datastore_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->get_containers: %s\n" % e)