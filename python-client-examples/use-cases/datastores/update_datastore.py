"""
Example script demonstrating how to update a JDBC datastore using the Qualytics API swagger client.

This example uses requests library directly since the swagger client has serialization
issues with the connection/connection_id pattern.
"""

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


def update_jdbc_datastore_example(datastore_id, connection_id):
    """
    Update a JDBC datastore's configuration.

    Args:
        datastore_id (int): The ID of the datastore to update
        connection_id (int): The connection ID to use (from the existing datastore)

    Update the parameters below with your desired changes.

    Note: Uses requests library directly since the swagger client has serialization issues.
    For updates, you must provide connection_id (not a full connection object).
    """
    # Build the request body as a dict
    # Note: For updates, use connection_id instead of a full connection object
    body = {
        "type": "postgresql",
        "name": "swagger Updated PostgreSQL Datastore",
        "enrichment_only": False,
        "enrichment_prefix": "_qualytics",  # Required field
        "tags": ["updated", "staging"],
        "connection_id": connection_id,  # Reference existing connection by ID
        "database": "qualytics_dev_enrichment",
        "schema": "qualytics",
        "favorite": False
    }

    try:
        # Use requests library directly
        import requests

        # Construct the URL
        base_host = api_instance.api_client.configuration.host
        if base_host.endswith('/api'):
            url = f"{base_host}/datastores/{datastore_id}"
        else:
            url = f"{base_host}/api/datastores/{datastore_id}"

        headers = {
            "Authorization": f"Bearer {api_instance.api_client.configuration.access_token}",
            "Content-Type": "application/json"
        }

        # Use PUT to update datastore
        response = requests.put(url, headers=headers, json=body)

        if response.status_code in [200, 201]:
            print(f"Successfully updated JDBC datastore {datastore_id}")
            result = response.json()
            pprint(result)
            return result
        else:
            print(f"Failed to update datastore: {response.text}")
            return None
    except Exception as e:
        print("Exception when updating JDBC datastore: %s\n" % e)
        return None


if __name__ == '__main__':
    # Update these with your actual IDs
    DATASTORE_ID = 1703  # Replace with actual datastore ID
    CONNECTION_ID = 284  # Replace with the connection ID from your datastore

    # Uncomment the line below to run:
    update_jdbc_datastore_example(DATASTORE_ID, CONNECTION_ID)

    print("\nPlease uncomment the example function call above to run.")
    print("Make sure to update DATASTORE_ID and CONNECTION_ID before running.")
    print("\nTo get the connection_id, first retrieve the datastore using get_datastores.py")