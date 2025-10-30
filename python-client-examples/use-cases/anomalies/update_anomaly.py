"""
Example script demonstrating how to update anomalies using the Qualytics API swagger client.

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

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# Create an instance of the API class using CustomApiClient
# The CustomApiClient handles lenient deserialization to avoid validation errors
api_instance = swagger_client.AnomaliesApi(CustomApiClient(configuration))


def update_anomaly_status_example(anomaly_id, status, tags=None):
    """
    Update the status of a single anomaly (acknowledge or resolve).

    This demonstrates using the old-style Swagger UpdateAnomaly model.

    Args:
        anomaly_id (int): The ID of the anomaly to update
        status (str): New status - 'Acknowledged'
        tags (list): Optional list of tags to apply
    """
    # Create the old-style Swagger model instance
    body = swagger_client.UpdateAnomaly(
        status=status,  # Required: 'Acknowledged'
        tags=tags       # Optional: list of tags
    )

    try:
        # Call the API using the swagger client
        api_response = api_instance.update_anomaly(body=body, id=anomaly_id)

        print(f"Successfully updated anomaly {anomaly_id} to status: {status}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling AnomaliesApi->update_anomaly: %s\n" % e)
        return None


def bulk_update_anomalies_example(anomaly_ids, status, tags=None):
    """
    Bulk update multiple anomalies at once.

    Note: Uses PATCH (not PUT) for bulk updates. Due to serialization issues
    with the swagger client's bulk update, this uses requests library directly
    but still leverages swagger configuration for auth and base URL.

    Args:
        anomaly_ids (list): List of anomaly IDs to update
        status (str): New status - 'Acknowledged', 'Active', 'Resolved', 'Invalid', or 'Duplicate'
        tags (list): Optional list of tags to add to all anomalies
    """
    # Build the request body as a list of dicts (matching the API spec)
    body = []
    for anomaly_id in anomaly_ids:
        anomaly_update = {
            "id": anomaly_id,
            "status": status
        }
        if tags:
            anomaly_update["tags"] = tags
        body.append(anomaly_update)

    try:
        # Use requests library directly (swagger client has issues with bulk update)
        import requests

        # Construct the URL - handle cases where host may or may not include /api
        base_host = api_instance.api_client.configuration.host
        if base_host.endswith('/api'):
            url = f"{base_host}/anomalies"
        else:
            url = f"{base_host}/api/anomalies"

        headers = {
            "Authorization": f"Bearer {api_instance.api_client.configuration.access_token}",
            "Content-Type": "application/json"
        }

        # Use PATCH for bulk updates (not PUT)
        response = requests.patch(url, headers=headers, json=body)

        if response.status_code in [200, 201]:
            print(f"Successfully updated {len(anomaly_ids)} anomalies to status: {status}")
            result = response.json()
            pprint(result)
            return result
        else:
            print(f"Failed to bulk update anomalies: {response.text}")
            return None
    except Exception as e:
        print("Exception when bulk updating anomalies: %s\n" % e)
        return None


if __name__ == '__main__':
    # Uncomment the example you want to run:

    # Example 1: Acknowledge a single anomaly
    # update_anomaly_status_example(556034, "Acknowledged")

    # Example 2: Acknowledge an anomaly with tags
    # update_anomaly_status_example(556035, "Acknowledged", tags=["test swagger"])

    # Example 3: Bulk update multiple anomalies
    # bulk_update_anomalies_example([556037, 556042, 556050], "Acknowledged")

    # Example 4: Bulk update with tags
    bulk_update_anomalies_example([556053, 556054], "Acknowledged", tags=["test swagger bulk"])

    print("\nPlease uncomment one of the example function calls above to run.")
