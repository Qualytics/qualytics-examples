from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.DataStoresApi(swagger_client.ApiClient(configuration))

# Update the payload with the specifics for your enrichment datastore.  See the official docs (Note that "demo" can be replaed in this URL to load the docs from your deployment) for the expected schema and valid values: https://demo.qualytics.io/api/docs#tag/data-stores/operation/create_data_store
body = {
	"name": "Name of your enrichment",
	"type": "wasb",
	"uri": "wasb[s]://file_system@account_name.dfs.core.windows.net/<path>",
	"account_name": "",
	"access_key":"",
    "enrich_only": True
}

try:
    # Create Data Store
    api_response = api_instance.create_data_store(body)

    pprint(api_response)

except ApiException as e:
    print("Exception when calling DataStoresApi->create_data_store: %s\n" % e)