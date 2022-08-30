from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.DataStoresApi(swagger_client.ApiClient(configuration))

data_store_id = 0
data = {
	"type": "wasb",
    "name": "new name for my datastore"
}
body = swagger_client.DataStore1() # DataStore1 |


try:
    # Update Data Store
    api_response = api_instance.update_data_store(data, data_store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->update_data_store: %s\n" % e)