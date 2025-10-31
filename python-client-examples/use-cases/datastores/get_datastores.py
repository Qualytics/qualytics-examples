from __future__ import print_function
import sys
import os
from pprint import pprint

# Add the parent directory to the path so we can import swagger_client
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.custom_api_client import CustomApiClient

# Configure API client with credentials from .env file
# The configuration reads API_TOKEN (Personal Access Token) and API_BASE_URL from the environment
configuration = swagger_client.Configuration()

# Create an instance of the API class using CustomApiClient
# The CustomApiClient handles lenient deserialization to avoid validation errors
api_instance = swagger_client.DatastoresApi(CustomApiClient(configuration))

try:
    # Get all datastores
    api_response = api_instance.get_datastores()

    # Handle response - could be an object or a dict
    if isinstance(api_response, dict):
        items_count = len(api_response.get('items', []))
    elif hasattr(api_response, 'items') and not callable(api_response.items):
        items_count = len(api_response.items)
    else:
        items_count = 'N/A'

    print(f"Retrieved {items_count} datastores")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatastoresApi->get_datastores: %s\n" % e)
