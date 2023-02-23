from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# Update the payloads with the specifics for your needs.  See the official docs (Note that "demo" can be replaed in this URL to load the docs from your deployment) for the expected schema and valid values: https://demo.qualytics.io/api/docs#tag/quality-checks/operation/create_quality_check
data = {
	"container_id": 0,
	"fields": [
		"field_name"
	],
	"description": "Is not Null",
	"rule": "notNull",
	"coverage": 1
}
# create an instance of the API class
api_instance = swagger_client.QualityChecksApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateQualityCheck(**data) # CreateQualityCheck |

try:
    # Create Quality Check
    api_response = api_instance.create_quality_check(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityChecksApi->create_quality_check: %s\n" % e)