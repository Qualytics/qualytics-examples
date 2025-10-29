from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.DatastoresApi(swagger_client.ApiClient(configuration))

# Update the payload with the specifics for your enrichment datastore.  See the official docs (Note that "demo" can be replaed in this URL to load the docs from your deployment) for the expected schema and valid values: https://demo.qualytics.io/api/docs#tag/datastores/operation/create_datastore
body = {
	"name": "Name of your enrichment",
	"type": "wasb",
	"uri": "wasb[s]://file_system@account_name.dfs.core.windows.net/<path>",
	"account_name": "",
	"access_key":"",
    "enrich_only": True
}

try:
    # Create Datastore
    api_response = api_instance.create_datastore(body)

    pprint(api_response)

except ApiException as e:
    print("Exception when calling DatastoresApi->create_datastore: %s\n" % e)