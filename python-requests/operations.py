import requests
import json
import time

# Define the base URL for the API
BASE_URL = "https://develop.qualytics.io/api"
#"YOUR_DEPLOYMENT_URL"  # ex: https://acme.qualytics.io/api

# Secrets for Auth Token
PERSONAL_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGQiOnsiaWQiOiJnb29nbGUtYXBwc3xndXN0YXZvQHF1YWx5dGljcy5jbyIsImVtYWlsIjoiZ3VzdGF2b0BxdWFseXRpY3MuY28iLCJuYW1lIjoiR3VzdGF2byBDYXJkb3NvIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BTFYtVWpXSzA3TWJVZ1kwTjRBRHlSRk5HTkRlTzRvcUhvSHJyMmFBMW84YlFGWnNuWU1FeVRZZDRkRkhZOFlBV0dUb0czLWtWQmxRWFY0bkJGZmQ2bENlTGY5eUJvSTlNYlphTWxqWk1fYzJnYU95cFdHSHdXOE1USXhoUHAzaWFuRW1sQmhqT1FoTWh2S2JlMGstcDgzU293SG5hSDRQWGVGNnhoZThhQ3hXMnVJRVhYZm50S2did1gwbmRSaDZyd0NIVHU4VmNfWEJ0WkdldHJlN2pfWWRUUzBKOWpaY20zUnZsaEFJU3pqd0pxN0ExcE5fRy1ER3BSaTE3ZkMySzVjY25zNU5HRmp0dzBwQUNDNVkxS1BudkREVVRrZ2ViUjlpRjQxdzRlTjh5T3FVNTNnUkFac01mOFdTSExqazhRdmVnM2t0UF9OX2ZYSjdBYmlpSXVRQ0lDMENRWkg5eDJJYWhGVENqTVVuUXZhUUVFblU1SGxJanZrWDQ5dEFFZFhGVlVZWm9yaFhhVVhaWkp1LWJFZnVUMVJpaHJqdUtraXlMQXExR2VtVE04ZmZTZkE3WVZOTDY5SThUd3NZOEYyWGMwYmFra3Zmcmhja2IzMlpwMFBVMTAyY1hMZFJqU3Rnamk2eXk4bDYxdG9wSm5zeGc5MlR0QjJZS1RGcExkWjNCUXdUWGZmeTFuMFNKbDBncFd6dU5IanRkZHJ3OWgzUTZacmR5MGZWMWprbG43dnB3cXRvUTRpQXVLWExuMlZEdC1HZTJsWWhyQk9DQU1qNzJKd1FsWEZCX2ItYVBCNDJqNF8xc0xyVl96YnZ2RWNRNnFOeWZSN2Nmd1YyMkpQal9UQjZyMVFzU2ppUVhaWDYwQnZvZmV2SGNBcVROelZwOVV2eGFEZXRfZ1dMQWlUczZLMU50M0xlVGlEZ3pYYldDR0pnSS1yeTBEY0cxOFZ4T2pxOTlsMnJWSFR0YmdqUEZTUzlwcWdTTUJGNlR2YnBnUzkxR1hZWFFpMTlNSFdXRGduZDZxajFOaXk2LTFnQzhkdHBBZzFkRHpoeTl0UWV1MktCMHBydjlRQk1XZVdxbXBlSW82NF9scTd5S2pkdExfUXZyZDBobEx6YVYyakZNUV9KTmNUaXlaaTVGMVBaWHdEbnUwUVVMVXd2ZThwRDBJZmxMUEw1S2NuZThRRnFISmRjbTl3bEg5djJVeUhvRG83V2Zrcjc0OU1WdDc0QXRTemhscVVXNHJUVFNVRE1UWnNVQWpRb0xnWlJSdzBTU1VSUkpxdjg1d3BhdUstdjM0T2VSckMxT0d4d2tKS2ZIclBxZlMwLVczUVRtLWxWPXM5Ni1jIiwic2NpbV9yZXN0cmljdGVkIjpmYWxzZX0sInN1YiI6Imdvb2dsZS1hcHBzfGd1c3Rhdm9AcXVhbHl0aWNzLmNvIiwiaXNzIjoiaHR0cHM6Ly9xdWFseXRpY3MuaW8iLCJjcnQiOiIyMDI1LTEwLTE0VDE1OjU0OjAxLjk0NzIwOSswMDowMCIsImV4cCI6MTc2MzA0OTI0MX0.lOzgbMTR94MnFYY6d-s4DSYckk5xjMYZgE7x7Fg1eMo"
#"YOUR_TOKEN_HERE"


def _get_default_headers():
    return {
        "Authorization": f"Bearer {PERSONAL_ACCESS_TOKEN}"
    }


def _pprint(text):
    print(json.dumps(json.loads(text), indent=2))


# End Helper functions

# Start API functions
def run_catalog_operation(datastore_id):
    """
    Trigger a catalog operation to discover containers in a datastore.

    Args:
        datastore_id (int): The ID of the datastore to catalog

    Returns:
        dict: The operation response containing the operation ID
    """
    # Define the full URL for the endpoint
    endpoint = "operations/run"
    url = f"{BASE_URL}/{endpoint}"

    # Define the request body for catalog operation
    body = {
        "type": "catalog",
        "datastore_id": datastore_id
    }

    # Make the request
    response = requests.post(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        operation_data = response.json()
        print(f"Catalog operation started successfully!")
        print(f"Operation ID: {operation_data.get('id')}")
        _pprint(response.content)
        return operation_data
    else:
        print(f"Failed to start catalog operation: {response.text}")
        return None


def run_profile_operation(datastore_id, container_ids=None):
    """
    Trigger a profile operation to analyze data patterns and statistics.

    Args:
        datastore_id (int): The ID of the datastore to profile
        container_ids (list): Optional list of specific container IDs to profile

    Returns:
        dict: The operation response containing the operation ID
    """
    # Define the full URL for the endpoint
    endpoint = "operations/run"
    url = f"{BASE_URL}/{endpoint}"

    # Define the request body for profile operation
    body = {
        "type": "profile",
        "datastore_id": datastore_id
    }

    # Add container filter if provided
    if container_ids:
        body["container_ids"] = container_ids

    # Make the request
    response = requests.post(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        operation_data = response.json()
        print(f"Profile operation started successfully!")
        print(f"Operation ID: {operation_data.get('id')}")
        _pprint(response.content)
        return operation_data
    else:
        print(f"Failed to start profile operation: {response.text}")
        return None


def run_scan_operation(datastore_id, container_ids=None, incremental=True):
    """
    Trigger a scan operation to detect data quality anomalies.

    Args:
        datastore_id (int): The ID of the datastore to scan
        container_ids (list): Optional list of specific container IDs to scan
        incremental (bool): Whether to run incremental scan (default: True)

    Returns:
        dict: The operation response containing the operation ID
    """
    # Define the full URL for the endpoint
    endpoint = "operations/run"
    url = f"{BASE_URL}/{endpoint}"

    # Define the request body for scan operation
    body = {
        "type": "scan",
        "datastore_id": datastore_id,
        "incremental": incremental
    }

    # Add container filter if provided
    if container_ids:
        body["container_ids"] = container_ids

    # Make the request
    response = requests.post(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        operation_data = response.json()
        scan_type = "Incremental" if incremental else "Full"
        print(f"{scan_type} scan operation started successfully!")
        print(f"Operation ID: {operation_data.get('id')}")
        _pprint(response.content)
        return operation_data
    else:
        print(f"Failed to start scan operation: {response.text}")
        return None


def get_operation_status(operation_id):
    """
    Check the status of a running or completed operation.

    Args:
        operation_id (int): The ID of the operation to check

    Returns:
        dict: The operation details including status
    """
    # Define the full URL for the endpoint
    endpoint = f"operations/{operation_id}"
    url = f"{BASE_URL}/{endpoint}"

    # Make the request
    response = requests.get(url, headers=_get_default_headers())

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        operation_data = response.json()
        status = operation_data.get('status', 'unknown')
        print(f"Operation {operation_id} status: {status}")
        _pprint(response.content)
        return operation_data
    else:
        print(f"Failed to get operation status: {response.text}")
        return None


def get_recent_operations(datastore_id=None, operation_type=None, limit=20):
    """
    Get a list of recent operations with optional filters.

    Args:
        datastore_id (int): Filter by datastore ID
        operation_type (str): Filter by operation type - 'catalog', 'profile', 'scan'
        limit (int): Maximum number of results to return
    """
    # Define the full URL for the endpoint
    endpoint = "operations"
    url = f"{BASE_URL}/{endpoint}"

    # Define parameters
    params = {
        "limit": limit,
        "sort_created": "desc"
    }

    # Add optional filters
    if datastore_id:
        params["datastore"] = datastore_id
    if operation_type:
        params["type"] = operation_type

    # Make the request
    response = requests.get(url, headers=_get_default_headers(), params=params)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    _pprint(response.content)


def wait_for_operation(operation_id, timeout=300, poll_interval=10):
    """
    Wait for an operation to complete, polling for status updates.

    Args:
        operation_id (int): The ID of the operation to monitor
        timeout (int): Maximum time to wait in seconds (default: 300)
        poll_interval (int): Time between status checks in seconds (default: 10)

    Returns:
        dict: The final operation details, or None if timeout
    """
    print(f"Waiting for operation {operation_id} to complete...")
    start_time = time.time()

    while True:
        # Check if timeout exceeded
        if time.time() - start_time > timeout:
            print(f"Timeout exceeded after {timeout} seconds")
            return None

        # Get operation status
        operation = get_operation_status(operation_id)

        if operation:
            status = operation.get('status', 'unknown')

            # Check if operation is complete
            if status in ['completed', 'success', 'succeeded']:
                print(f"Operation {operation_id} completed successfully!")
                return operation
            elif status in ['failed', 'error']:
                print(f"Operation {operation_id} failed!")
                return operation
            else:
                print(f"Operation status: {status}. Checking again in {poll_interval} seconds...")

        # Wait before next check
        time.sleep(poll_interval)


def abort_operation(operation_id):
    """
    Abort a running operation.

    Args:
        operation_id (int): The ID of the operation to abort
    """
    # Define the full URL for the endpoint
    endpoint = f"operations/abort/{operation_id}"
    url = f"{BASE_URL}/{endpoint}"

    # Make the request
    response = requests.put(url, headers=_get_default_headers())

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Operation {operation_id} aborted successfully")
        _pprint(response.content)
    else:
        print(f"Failed to abort operation: {response.text}")


# End API functions

# Main
def main():
    # Example 1: Run a catalog operation
    # operation = run_catalog_operation(datastore_id=1734)

    # Example 2: Run a profile operation
    # operation = run_profile_operation(datastore_id=1734)

    # Example 3: Run a profile operation on specific containers
    # operation = run_profile_operation(datastore_id=1734, container_ids=[43664, 43667])

    # Example 4: Run an incremental scan
    # operation = run_scan_operation(datastore_id=1734, incremental=True)

    # Example 5: Run a full scan
    # operation = run_scan_operation(datastore_id=1734, incremental=False)

    # Example 6: Check operation status
    # get_operation_status(operation_id=75962)

    # Example 7: Get recent operations for a datastore
    # get_recent_operations(datastore_id=1734, limit=5)

    # Example 8: Get recent scan operations
    # get_recent_operations(operation_type="scan", limit=10)

    # Example 9: Wait for operation to complete
    # wait_for_operation(operation_id=75962, timeout=600, poll_interval=15)

    # Example 10: Abort a running operation
    # abort_operation(operation_id=75962)

    # Uncomment one of the examples above to run
    print("Please uncomment one of the example function calls in main() to run")


if __name__ == '__main__':
    main()
