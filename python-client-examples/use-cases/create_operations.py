from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# Update the payloads with the specifics for your needs.  See the official docs (Note that "demo" can be replaed in this URL to load the docs from your deployment) for the expected schema and valid values: https://demo.qualytics.io/api/docs#tag/operations/operation/create_operation
data_profile = {
	"datastore_id": 0,
	"type": "profile",
	"infer_constraints": True
}
data_scan = {
	"datastore_id": 0,
	"type": "scan",
	"infer_constraints": True
}

data_catalog = {
    "datastore_id": 0,
    "type": "catalog",
    "infer_constraints": True
}
# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Operation3() # Operation3 |

try:
    # Create Operation
    api_response = api_instance.create_operation(data_profile) # [profile| scan| catalog]
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->create_operation: %s\n" % e)