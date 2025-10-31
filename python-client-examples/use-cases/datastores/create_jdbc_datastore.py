"""
Example script demonstrating how to create a datastore using the Qualytics API swagger client.

This example uses old-style Swagger models (CreateDfsDatastore, CreateJdbcDatastore, CreateQfsDatastore)
since the datastore models were generated with the older Swagger Codegen tool.
The CustomApiClient is used to handle lenient deserialization.
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

def create_jdbc_datastore_example():
    """
    Create a JDBC datastore - supports relational databases like PostgreSQL, MySQL, etc.

    Update the parameters below with your actual database credentials.

    Note: Uses requests library directly since the swagger client has serialization
    issues with the connection/connection_id pattern.
    """
    # Build the request body as a dict with nested connection object
    # The API expects either "connection" (with nested credentials) or "connection_id"
    body = {
        "type": "postgresql",  # JDBC type: postgresql, mysql, oracle, sqlserver, etc.
        "name": "swagger PostgreSQL Datastore",
        "enrich_only": False,
        "tags": ["example", "postgres"],
        "connection": {
            "type": "postgresql",  # Connection type must match datastore type
            "host": "hostname",
            "port": "port",
            "username": "postgres",
            "password": "postgres"
        },
        "database": "db_name",
        "schema": "db_schema",
    }

    try:
        # Use requests library directly
        import requests

        # Construct the URL
        base_host = api_instance.api_client.configuration.host
        if base_host.endswith('/api'):
            url = f"{base_host}/datastores"
        else:
            url = f"{base_host}/api/datastores"

        headers = {
            "Authorization": f"Bearer {api_instance.api_client.configuration.access_token}",
            "Content-Type": "application/json"
        }

        # Use POST to create datastore
        response = requests.post(url, headers=headers, json=body)

        if response.status_code in [200, 201]:
            print("Successfully created JDBC datastore")
            result = response.json()
            pprint(result)
            return result
        else:
            print(f"Failed to create datastore: {response.text}")
            return None
    except Exception as e:
        print("Exception when creating JDBC datastore: %s\n" % e)
        return None

if __name__ == '__main__':
    create_jdbc_datastore_example()

    print("\nPlease uncomment one of the example function calls above to run.")
    print("Make sure to update the credentials and connection details before running.")