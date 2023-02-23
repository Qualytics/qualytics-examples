from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.DatastoresApi(swagger_client.ApiClient(configuration))

datastore_id = 0
data = {
	"type": "wasb",
    "name": "new name for my datastore"
}
body = swagger_client.Datastore1() # Datastore1 |


try:
    # Update Datastore
    api_response = api_instance.update_datastore(data, datastore_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatastoresApi->update_datastore: %s\n" % e)