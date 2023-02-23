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
	"name": "New Name of your Datastore",
	"type": "wasb",
	"uri": "wasb[s]://file_system@account_name.dfs.core.windows.net/<path>",
    "enrich_only": False,
    "enrich_container_prefix": "_name_of_your_datastore",
	"access_key": "",
	"secret_key":None
}
body = swagger_client.Datastore1() # Datastore1 |


try:
    # Update Datastore
    api_response = api_instance.update_datastore(data, datastore_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatastoresApi->update_datastore: %s\n" % e)