"""
Example script demonstrating how to create computed containers using the Qualytics API
swagger client with Pydantic models.

This example uses a CustomApiClient that extends the generated swagger client to support
both old-style Swagger models and new Pydantic models. This approach avoids modifying
auto-generated files which would be overwritten on regeneration.
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

# Create an instance of the API class using our CustomApiClient
# This custom client supports both old Swagger models and new Pydantic models
api_instance = swagger_client.ContainersApi(CustomApiClient(configuration))

def create_computed_table_example():
    """
    Create a computed table container using a SQL query.
    This creates a virtual table based on a SELECT query.
    """
    # Create the model instance
    body = swagger_client.CreateComputedTableContainer(
        container_type="computed_table",
        datastore_id=1734,
        name="swagger computed table",
        query="select * from nation"
        # Optional: additional_metadata={"key": "value"}
    )

    try:
        # Create container using the swagger client
        # The CustomApiClient handles both Pydantic serialization (request)
        # and lenient deserialization (response) to work with mixed model types
        api_response = api_instance.create_container(body=body)
        print("Container created successfully!")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling ContainersApi->create_container: %s\n" % e)
        return None
    
if __name__ == '__main__':
    create_computed_table_example()