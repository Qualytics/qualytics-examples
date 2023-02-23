from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# Update the payloads with the specifics for your needs.  See the official docs (Note that "demo" can be replaed in this URL to load the docs from your deployment) for the expected schema and valid values: https://demo.qualytics.io/api/docs#tag/operations/operation/create_schedule_operation
data_catalog = {
  "crontab": "*/10 * * * *",
  "type": "catalog",
  "datastore_id": 193
}
data_profile = {
  "crontab": "*/10 * * * *",
  "type": "profile",
  "datastore_id": 193
}

data_scan = {
  "crontab": "*/10 * * * *",
  "type": "scan",
  "datastore_id": 0
}
# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Operation1() # Operation1 |

try:
    # Create Schedule Operation
    api_response = api_instance.create_schedule_operation(data_profile) # [profile | catalog| scan]
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->create_schedule_operation: %s\n" % e)