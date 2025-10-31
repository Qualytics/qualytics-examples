"""
Example script demonstrating how to retrieve quality checks using the Qualytics API swagger client.

This example shows how to fetch quality checks with various filters like datastore, container,
field, rule type, and tags.

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


def get_quality_checks_example(datastore=None, container=None, field=None, rule_type=None,
                                inferred=None, tag=None, page=1, size=50):
    """
    Get a list of quality checks with optional filters.

    Args:
        datastore (int): Filter by datastore ID
        container (list[int] or int): Filter by container ID(s)
        field (list[str] or str): Filter by field name(s)
        rule_type (list[str] or str): Filter by rule type(s) (e.g., 'notNull', 'unique')
        inferred (bool): Filter by inferred status (True for inferred, False for user-created)
        tag (list[str] or str): Filter by tag(s)
        page (int): Page number (default: 1)
        size (int): Number of results per page (default: 50)

    Returns:
        dict: Paginated response with quality checks
    """
    try:
        # Build parameters dictionary
        params = {
            'page': page,
            'size': size,
        }

        # Add optional filters
        if datastore is not None:
            params['datastore'] = datastore
        if container is not None:
            params['container'] = [container] if isinstance(container, int) else container
        if field is not None:
            params['field'] = [field] if isinstance(field, str) else field
        if rule_type is not None:
            params['rule_type'] = [rule_type] if isinstance(rule_type, str) else rule_type
        if inferred is not None:
            params['inferred'] = inferred
        if tag is not None:
            params['tag'] = [tag] if isinstance(tag, str) else tag

        # Call the API using the swagger client
        # See the official docs for more details:
        # https://demo.qualytics.io/api/docs#tag/quality-checks/operation/get_quality_checks
        api_response = api_instance.get_quality_checks(**params)

        # Handle response - the API returns a paginated response
        if isinstance(api_response, dict):
            # Paginated response with 'items' field
            items = api_response.get('items', [])
            total = api_response.get('total', 0)
            current_page = api_response.get('page', page)
            pages = api_response.get('pages', 0)

            print(f"Retrieved {len(items)} quality check(s) on page {current_page} of {pages} (total: {total})")
            if items:
                print("\nQuality Checks:")
                pprint(items)
            else:
                print("No quality checks found.")
            return api_response
        else:
            # Handle object response (if deserialization succeeded)
            if hasattr(api_response, 'items') and not callable(api_response.items):
                items = api_response.items
                total = getattr(api_response, 'total', 0)
                current_page = getattr(api_response, 'page', page)
                pages = getattr(api_response, 'pages', 0)

                print(f"Retrieved {len(items)} quality check(s) on page {current_page} of {pages} (total: {total})")
                pprint(api_response)
            else:
                print("Retrieved quality checks")
                pprint(api_response)
            return api_response
    except ApiException as e:
        print("Exception when calling QualityChecksApi->get_quality_checks: %s\n" % e)
        return None


def get_quality_checks_by_datastore_example(datastore_id):
    """
    Get all quality checks for a specific datastore.

    Args:
        datastore_id (int): The ID of the datastore

    Returns:
        dict: Quality checks for the datastore
    """
    print(f"\n=== Getting quality checks for datastore {datastore_id} ===")
    return get_quality_checks_example(datastore=datastore_id, size=100)


def get_quality_checks_by_container_example(container_id):
    """
    Get all quality checks for a specific container.

    Args:
        container_id (int): The ID of the container

    Returns:
        dict: Quality checks for the container
    """
    print(f"\n=== Getting quality checks for container {container_id} ===")
    return get_quality_checks_example(container=container_id, size=100)


def get_inferred_quality_checks_example(datastore_id=None):
    """
    Get all inferred (automatically created) quality checks.

    Args:
        datastore_id (int): Optional datastore ID to filter by

    Returns:
        dict: Inferred quality checks
    """
    print(f"\n=== Getting inferred quality checks ===")
    return get_quality_checks_example(datastore=datastore_id, inferred=True, size=100)


def get_quality_checks_by_rule_type_example(rule_type, datastore_id=None):
    """
    Get quality checks by rule type.

    Args:
        rule_type (str or list): Rule type(s) to filter by (e.g., 'notNull', 'unique')
        datastore_id (int): Optional datastore ID to filter by

    Returns:
        dict: Quality checks matching the rule type
    """
    print(f"\n=== Getting quality checks with rule type: {rule_type} ===")
    return get_quality_checks_example(datastore=datastore_id, rule_type=rule_type, size=100)


if __name__ == '__main__':
    # Update these values with your actual IDs
    DATASTORE_ID = 1734  # Replace with your actual datastore ID
    CONTAINER_ID = 43664  # Replace with your actual container ID

    # Uncomment the example you want to run:

    # Example 1: Get all quality checks with pagination
    # get_quality_checks_example(page=1, size=50)

    # Example 2: Get quality checks for a specific datastore
    # get_quality_checks_by_datastore_example(DATASTORE_ID)

    # Example 3: Get quality checks for a specific container
    # get_quality_checks_by_container_example(CONTAINER_ID)

    # Example 4: Get only inferred quality checks
    # get_inferred_quality_checks_example(DATASTORE_ID)

    # Example 5: Get quality checks by rule type
    # get_quality_checks_by_rule_type_example('notNull', DATASTORE_ID)

    # Example 6: Get quality checks with multiple filters
    get_quality_checks_example(
        datastore=DATASTORE_ID,
        inferred=False,  # Only user-created checks
        rule_type=['notNull', 'unique'],
        page=1,
        size=100
    )

    print("\nPlease update DATASTORE_ID and CONTAINER_ID, then uncomment one of the example function calls above to run.")
