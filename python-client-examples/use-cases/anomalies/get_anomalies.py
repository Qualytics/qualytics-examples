"""
Example script demonstrating how to retrieve anomalies using the Qualytics API swagger client.

This example uses old-style Swagger models (not Pydantic) since the anomaly models
were generated with the older Swagger Codegen tool. The CustomApiClient is used to
handle lenient deserialization of responses that may not match model validation.
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
api_instance = swagger_client.AnomaliesApi(CustomApiClient(configuration))


def get_anomalies_example(status=None, datastore_id=None, container_id=None, size=100):
    """
    Get a list of anomalies with optional filters.

    Args:
        status (str or list): Filter by status - single value like 'Active' or list like ['Active', 'Acknowledged']
        datastore_id (int): Filter by datastore ID
        container_id (int): Filter by container ID
        size (int): Maximum number of results to return
    """
    try:
        # Build parameters dictionary
        params = {
            'size': size,
        }

        # Add optional filters
        # Note: status must be a list per API spec
        if status:
            if isinstance(status, str):
                params['status'] = [status]  # Convert single string to list
            else:
                params['status'] = status  # Already a list
        if datastore_id:
            params['datastore'] = datastore_id
        if container_id:
            params['container'] = [container_id] if isinstance(container_id, int) else container_id  # Also expects list

        # Call the API using the swagger client
        api_response = api_instance.get_anomalies(**params)

        # Handle response - could be an object or a dict (if deserialization failed)
        if isinstance(api_response, dict):
            # Raw dict response from CustomApiClient
            items_count = len(api_response.get('items', []))
        elif hasattr(api_response, 'items') and not callable(api_response.items):
            # Object with items attribute
            items_count = len(api_response.items)
        else:
            items_count = 'N/A'

        print(f"Retrieved {items_count} anomalies")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling AnomaliesApi->get_anomalies: %s\n" % e)
        return None


def get_anomaly_by_id_example(anomaly_id):
    """
    Get detailed information about a specific anomaly.

    Args:
        anomaly_id (int): The ID of the anomaly to retrieve
    """
    try:
        # Call the API using the swagger client
        api_response = api_instance.get_anomaly_by_id(id=anomaly_id)

        print(f"Retrieved anomaly {anomaly_id}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling AnomaliesApi->get_anomaly_by_id: %s\n" % e)
        return None


def get_anomaly_source_record_example(anomaly_id):
    """
    Get the source record associated with an anomaly.

    Args:
        anomaly_id (int): The ID of the anomaly
    """
    try:
        # Call the API using the swagger client
        api_response = api_instance.get_anomaly_source_record(
            id=anomaly_id,
        )

        print(f"Retrieved source record for anomaly {anomaly_id}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling AnomaliesApi->get_anomaly_source_record: %s\n" % e)
        return None


if __name__ == '__main__':
    # Uncomment the example you want to run:

    # Example 1: Get all Active anomalies
    # get_anomalies_example(status="Active", size=50)

    # Example 1b: Get anomalies with multiple statuses
    # get_anomalies_example(status=["Active", "Acknowledged"], size=5)

    # Example 2: Get anomalies for a specific datastore
    # get_anomalies_example(datastore_id=1734)

    # Example 3: Get anomalies for a specific container
    # get_anomalies_example(container_id=556037)

    # Example 4: Get details of a specific anomaly
    # get_anomaly_by_id_example(556037)

    # Example 5: Get source records for an anomaly
    get_anomaly_source_record_example(556037)

    print("\nPlease uncomment one of the example function calls above to run.")
