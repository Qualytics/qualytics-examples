"""
Example script demonstrating how to create quality checks using the Qualytics API swagger client.

This example shows how to create different types of quality checks with various rules.

This example uses old-style Swagger models since the quality check models were generated with
the older Swagger Codegen tool. The CustomApiClient is used to handle lenient deserialization
of responses that may not match model validation.
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

# Create an instance of the API class using CustomApiClient
# The CustomApiClient handles lenient deserialization to avoid validation errors
api_instance = swagger_client.QualityChecksApi(CustomApiClient(configuration))


def create_quality_check_example(container_id, field_name, rule, description, coverage=1.0, properties=None):
    """
    Create a quality check.

    Args:
        container_id (int): The ID of the container (table/file) to apply the check to
        field_name (str): The name of the field/column to check
        rule (str): The rule type (e.g., 'notNull', 'unique', 'positive', 'volumetric', etc.)
        description (str): Description of the quality check
        coverage (float): Coverage value between 0 and 1 (default: 1.0)
        properties (dict): Optional properties specific to the rule type

    Returns:
        GetQualityCheck or dict: The created quality check details
    """
    # Prepare the quality check data
    # See the official docs for the expected schema and valid values:
    # https://demo.qualytics.io/api/docs#tag/quality-checks/operation/create_quality_check
    data = {
        "container_id": container_id,
        "fields": [field_name],
        "description": description,
        "rule": rule,
        "coverage": coverage
    }

    # Add properties if provided
    if properties:
        data["properties"] = properties

    try:
        # Create the quality check
        # Note: The API accepts a dict directly, not a model instance
        api_response = api_instance.create_quality_check(data)

        print(f"Quality check created successfully!")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling QualityChecksApi->create_quality_check: %s\n" % e)
        return None


def create_not_null_check_example(container_id, field_name):
    """
    Create a Not Null quality check.

    Args:
        container_id (int): The ID of the container
        field_name (str): The name of the field

    Returns:
        The created quality check
    """
    return create_quality_check_example(
        container_id=container_id,
        field_name=field_name,
        rule="notNull",
        description=f"Checks that {field_name} is not null",
        coverage=1.0
    )


def create_unique_check_example(container_id, field_name):
    """
    Create a Unique quality check.

    Args:
        container_id (int): The ID of the container
        field_name (str): The name of the field

    Returns:
        The created quality check
    """
    return create_quality_check_example(
        container_id=container_id,
        field_name=field_name,
        rule="unique",
        description=f"Checks that {field_name} values are unique",
        coverage=1.0
    )


def create_positive_check_example(container_id, field_name):
    """
    Create a Positive (numeric) quality check.

    Args:
        container_id (int): The ID of the container
        field_name (str): The name of the field

    Returns:
        The created quality check
    """
    return create_quality_check_example(
        container_id=container_id,
        field_name=field_name,
        rule="positive",
        description=f"Checks that {field_name} contains positive values",
        coverage=1.0
    )

if __name__ == '__main__':
    # Update these values with your actual container_id and field names
    CONTAINER_ID = 43664  # Replace with your actual container ID
    FIELD_NAME = "BUSINESS_ID"  # Replace with your actual field name

    # Uncomment the example you want to run:

    # Example 1: Create a Not Null check
    # create_not_null_check_example(CONTAINER_ID, FIELD_NAME)

    # Example 2: Create a Unique check
    # create_unique_check_example(CONTAINER_ID, FIELD_NAME)

    # Example 3: Create a Positive check (for numeric fields)
    # create_positive_check_example(CONTAINER_ID, FIELD_NAME)

    # Example 4: Create a custom check with specific parameters
    create_quality_check_example(
        container_id=CONTAINER_ID,
        field_name=FIELD_NAME,
        rule="notNull",
        description="Custom quality check description",
        coverage=0.95
    )

    print("\nPlease update CONTAINER_ID and FIELD_NAME, then uncomment one of the example function calls above to run.")
