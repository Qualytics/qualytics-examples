"""
Example script demonstrating how to update containers using the Qualytics API
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

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# Create an instance of the API class using our CustomApiClient
# This custom client supports both old Swagger models and new Pydantic models
api_instance = swagger_client.ContainersApi(CustomApiClient(configuration))

def update_computed_table_example():
    """
    Update an existing computed table container.
    You can update the name, query, tags, tracking settings, etc.
    """
    container_id = 45175

    # Create the update model instance
    body = swagger_client.UpdateComputedTableContainer(
        container_type="computed_table",  # Required discriminator
        name="updated_computed_table_name",
        query="SELECT * FROM nation",
        tags=["B2B"],
        # Optional: additional_metadata={"department": "finance"}
    )

    try:
        # Update container using the swagger client
        # The CustomApiClient handles both Pydantic serialization and lenient deserialization
        api_response = api_instance.update_container(body=body, id=container_id)
        print("Computed table container updated successfully!")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling ContainersApi->update_container: %s\n" % e)
        return None

if __name__ == '__main__':
    update_computed_table_example()