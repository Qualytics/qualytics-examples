import requests
import json

# Define the base URL for the API
BASE_URL = "YOUR_DEPLOYMENT_URL"  # ex: https://acme.qualytics.io/api

# Secrets for Auth Token
PERSONAL_ACCESS_TOKEN = "YOUR_TOKEN_HERE"


def _get_default_headers():
    return {
        "Authorization": f"Bearer {PERSONAL_ACCESS_TOKEN}"
    }


def _pprint(text):
    print(json.dumps(json.loads(text), indent=2))


# End Helper functions

# Start API functions
def get_anomalies(status=None, datastore_id=None, container_id=None, limit=100):
    """
    Get a list of anomalies with optional filters.

    Args:
        status (str): Filter by status - 'Acknowledged', 'new'
        datastore_id (int): Filter by datastore ID
        container_id (int): Filter by container ID
        limit (int): Maximum number of results to return
    """
    # Define the full URL for the endpoint
    endpoint = "anomalies"
    url = f"{BASE_URL}/{endpoint}"

    # Define parameters for the endpoint
    params = {
        "limit": limit,
        "sort_created": "desc"
    }

    # Add optional filters if provided
    if status:
        params["status"] = status
    if datastore_id:
        params["datastore"] = datastore_id
    if container_id:
        params["container"] = container_id

    # Make the request
    response = requests.get(url, headers=_get_default_headers(), params=params)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    _pprint(response.content)


def get_anomaly_by_id(anomaly_id):
    """
    Get detailed information about a specific anomaly.

    Args:
        anomaly_id (int): The ID of the anomaly to retrieve
    """
    # Define the full URL for the endpoint
    endpoint = "anomalies"
    url = f"{BASE_URL}/{endpoint}/{anomaly_id}"

    # Make the request
    response = requests.get(url, headers=_get_default_headers())

    # Print the response content
    print(f"Status Code: {response.status_code}")
    _pprint(response.content)


def update_anomaly_status(anomaly_id, status, comment=None):
    """
    Update the status of an anomaly (acknowledge or resolve).

    Args:
        anomaly_id (int): The ID of the anomaly to update
        status (str): New status - 'Acknowledged'
        comment (str): Optional comment explaining the status change
    """
    # Define the full URL for the endpoint
    endpoint = "anomalies"
    url = f"{BASE_URL}/{endpoint}/{anomaly_id}"

    # Define the request body
    body = {
        "status": status
    }

    if comment:
        body["comment"] = comment

    # Make the request
    response = requests.put(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Successfully updated anomaly {anomaly_id} to status: {status}")
        _pprint(response.content)
    else:
        print(f"Failed to update anomaly: {response.text}")


def get_anomaly_source_records(anomaly_id, limit=10):
    """
    Get source records associated with an anomaly.

    Args:
        anomaly_id (int): The ID of the anomaly
        limit (int): Maximum number of source records to return
    """
    # Define the full URL for the endpoint
    endpoint = f"anomalies/{anomaly_id}/source-record"
    url = f"{BASE_URL}/{endpoint}"

    # Define parameters
    params = {"limit": limit}

    # Make the request
    response = requests.get(url, headers=_get_default_headers(), params=params)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    _pprint(response.content)


def bulk_update_anomalies(anomaly_ids, status, tags=None):
    """
    Bulk update multiple anomalies at once.

    Args:
        anomaly_ids (list): List of anomaly IDs to update
        status (str): New status - 'Acknowledged'
        tags (list): Optional list of tags to add to all anomalies
    """
    # Define the full URL for the endpoint
    endpoint = "anomalies"
    url = f"{BASE_URL}/{endpoint}"

    # Define the request body - it expects a list of objects
    body = []
    for anomaly_id in anomaly_ids:
        anomaly_update = {
            "id": anomaly_id,
            "status": status
        }
        if tags:
            anomaly_update["tags"] = tags
        body.append(anomaly_update)

    # Make the request
    response = requests.put(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Successfully updated {len(anomaly_ids)} anomalies to status: {status}")
        _pprint(response.content)
    else:
        print(f"Failed to bulk update anomalies: {response.text}")


# End API functions

# Main
def main():
    # Example 1: Get all new anomalies
    # get_anomalies(status="new", limit=50)

    # Example 2: Get anomalies for a specific datastore
    # get_anomalies(datastore_id=844)

    # Example 3: Get anomalies for a specific container
    # get_anomalies(container_id=1234)

    # Example 4: Get details of a specific anomaly
    # get_anomaly_by_id(12345)

    # Example 5: Acknowledge an anomaly
    # update_anomaly_status(222824, "Acknowledged", comment="issue solved")

    # Example 6: Get source records for an anomaly
    get_anomaly_source_records(224448, limit=20)

    # Uncomment one of the examples above to run
    print("Please uncomment one of the example function calls in main() to run")


if __name__ == '__main__':
    main()
