from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# Update the payload with the specifics for your needs.  See the official docs (Note that "demo" can be replaed in this URL to load the docs from your deployment) for the expected schema and valid values: https://demo.qualytics.io/api/docs#tag/notifications/operation/create_notification_rule
body = {
  "name": "Anomaly Notification",
  "description": "Notification that triggers on anomalies",
  "trigger_type": "Anomaly",
  "tokenized_message": "Some anomaly found detected",
  "slack_webhook": "slack url",
  "tags": [
    "Critical"
  ]
}
# create an instance of the API class
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))


try:
    # Create Notification Rule
    api_response = api_instance.create_notification_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->create_notification_rule: %s\n" % e)