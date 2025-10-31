"""
Example script demonstrating how to run and manage operations using the Qualytics API swagger client.

This example uses old-style Swagger models (not Pydantic) since the operation models
were generated with the older Swagger Codegen tool. The CustomApiClient is used to
handle lenient deserialization of responses that may not match model validation.
"""

from __future__ import print_function
import sys
import os
import time
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
api_instance = swagger_client.OperationsApi(CustomApiClient(configuration))


def run_catalog_operation_example(datastore_id, recreate=False, prune=True, include=None):
    """
    Run a catalog operation to discover containers in a datastore.

    Args:
        datastore_id (int): The ID of the datastore to catalog
        recreate (bool): Whether to recreate the catalog from scratch
        prune (bool): Whether to remove containers no longer found in the source
        include (list): Optional list of container name patterns to include
    """
    # Create the old-style Swagger model instance
    body = swagger_client.CreateCatalogOperation(
        type='catalog',
        datastore_id=datastore_id,
        recreate=recreate,
        prune=prune,
        include=include
    )

    try:
        # Call the API using the swagger client
        api_response = api_instance.create_operation(body=body)

        print(f"Successfully started catalog operation for datastore {datastore_id}")

        # Handle response - could be an object or a dict
        if isinstance(api_response, dict):
            operation_id = api_response.get('id', 'N/A')
        elif hasattr(api_response, 'id'):
            operation_id = api_response.id
        else:
            operation_id = 'N/A'

        print(f"Operation ID: {operation_id}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->create_operation: %s\n" % e)
        return None


def run_profile_operation_example(datastore_id, container_names=None, infer_constraints=True,
                                   max_records_analyzed_per_partition=None):
    """
    Run a profile operation to analyze data quality and infer constraints.

    Args:
        datastore_id (int): The ID of the datastore to profile
        container_names (list): Optional list of specific container names to profile
        infer_constraints (bool): Whether to infer quality check constraints from the data
        max_records_analyzed_per_partition (int): Optional limit on records to analyze per partition
    """
    # Create the old-style Swagger model instance
    body = swagger_client.CreateProfileOperation(
        type='profile',
        datastore_id=datastore_id,
        container_names=container_names,
        infer_constraints=infer_constraints,
        max_records_analyzed_per_partition=max_records_analyzed_per_partition
    )

    try:
        # Call the API using the swagger client
        api_response = api_instance.create_operation(body=body)

        print(f"Successfully started profile operation for datastore {datastore_id}")

        # Handle response - could be an object or a dict
        if isinstance(api_response, dict):
            operation_id = api_response.get('id', 'N/A')
        elif hasattr(api_response, 'id'):
            operation_id = api_response.id
        else:
            operation_id = 'N/A'

        print(f"Operation ID: {operation_id}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->create_operation: %s\n" % e)
        return None


def run_scan_operation_example(datastore_id, container_names=None, incremental=True,
                                remediation='none', max_records_analyzed_per_partition=None):
    """
    Run a scan operation to check data against quality constraints.

    Args:
        datastore_id (int): The ID of the datastore to scan
        container_names (list): Optional list of specific container names to scan
        incremental (bool): Whether to scan only new/changed data since last scan
        remediation (str): Remediation strategy - 'none', 'anomaly', or 'record'
        max_records_analyzed_per_partition (int): Optional limit on records to analyze per partition
    """
    # Create the old-style Swagger model instance
    body = swagger_client.CreateScanOperation(
        type='scan',
        datastore_id=datastore_id,
        container_names=container_names,
        incremental=incremental,
        remediation=remediation,
        max_records_analyzed_per_partition=max_records_analyzed_per_partition
    )

    try:
        # Call the API using the swagger client
        api_response = api_instance.create_operation(body=body)

        print(f"Successfully started scan operation for datastore {datastore_id}")

        # Handle response - could be an object or a dict
        if isinstance(api_response, dict):
            operation_id = api_response.get('id', 'N/A')
        elif hasattr(api_response, 'id'):
            operation_id = api_response.id
        else:
            operation_id = 'N/A'

        print(f"Operation ID: {operation_id}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->create_operation: %s\n" % e)
        return None


def get_operation_by_id_example(operation_id):
    """
    Get the status and details of a specific operation.

    Args:
        operation_id (int): The ID of the operation to retrieve
    """
    try:
        # Call the API using the swagger client
        api_response = api_instance.get_operation(id=operation_id)

        print(f"Retrieved operation {operation_id}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->get_operation: %s\n" % e)
        return None


def get_recent_operations_example(datastore_id=None, operation_type=None, finished=None,
                                   result=None, page=1, size=20):
    """
    Get a list of recent operations with optional filters.

    Args:
        datastore_id (int): Filter by datastore ID
        operation_type (str): Filter by operation type - 'catalog', 'profile', or 'scan'
        finished (bool): Filter by finished status
        result (str): Filter by result - 'success' or 'failure'
        page (int): Page number for pagination (starts at 1, not 0)
        size (int): Number of results per page
    """
    try:
        # Build parameters dictionary
        params = {
            'page': page,
            'size': size,
        }

        # Add optional filters
        if datastore_id:
            params['datastore'] = datastore_id
        if operation_type:
            params['operation_type'] = operation_type
        if finished is not None:
            params['finished'] = finished
        if result:
            params['result'] = result

        # Call the API using the swagger client
        api_response = api_instance.get_operations(**params)

        # Handle response - could be an object or a dict
        if isinstance(api_response, dict):
            items_count = len(api_response.get('items', []))
        elif hasattr(api_response, 'items') and not callable(api_response.items):
            items_count = len(api_response.items)
        else:
            items_count = 'N/A'

        print(f"Retrieved {items_count} operations")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->get_operations: %s\n" % e)
        return None


def abort_operation_example(operation_id):
    """
    Abort a running operation.

    Args:
        operation_id (int): The ID of the operation to abort
    """
    try:
        # Call the API using the swagger client
        api_response = api_instance.abort_operation(id=operation_id)

        print(f"Successfully aborted operation {operation_id}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->abort_operation: %s\n" % e)
        return None


def wait_for_operation_example(operation_id, poll_interval=5, timeout=300):
    """
    Wait for an operation to complete by polling its status.

    Args:
        operation_id (int): The ID of the operation to wait for
        poll_interval (int): Seconds to wait between status checks
        timeout (int): Maximum seconds to wait before giving up

    Returns:
        The final operation response, or None if timeout/error
    """
    print(f"Waiting for operation {operation_id} to complete...")
    start_time = time.time()

    while True:
        try:
            # Get current operation status
            api_response = api_instance.get_operation(id=operation_id)

            # Extract status from response
            if isinstance(api_response, dict):
                status = api_response.get('status', {})
                finished = status.get('finished', False) if isinstance(status, dict) else False
                result = status.get('result') if isinstance(status, dict) else None
            elif hasattr(api_response, 'status'):
                status = api_response.status
                finished = getattr(status, 'finished', False) if status else False
                result = getattr(status, 'result', None) if status else None
            else:
                print("Warning: Could not determine operation status")
                finished = False
                result = None

            if finished:
                print(f"\nOperation {operation_id} completed with result: {result}")
                pprint(api_response)
                return api_response

            # Check timeout
            elapsed = time.time() - start_time
            if elapsed > timeout:
                print(f"\nTimeout waiting for operation {operation_id} after {timeout} seconds")
                return None

            # Wait before next poll
            print(f"Operation still running... (elapsed: {int(elapsed)}s)")
            time.sleep(poll_interval)

        except ApiException as e:
            print("Exception when polling operation status: %s\n" % e)
            return None


if __name__ == '__main__':
    # Uncomment the example you want to run:

    # Example 1: Run a catalog operation
    # run_catalog_operation_example(datastore_id=1734, recreate=False)

    # Example 2: Run a profile operation
    # run_profile_operation_example(datastore_id=1734, infer_constraints=True)

    # Example 3: Run a scan operation
    # run_scan_operation_example(datastore_id=1734, incremental=True)

    # Example 4: Run a scan on specific containers
    # run_scan_operation_example(datastore_id=1734, container_names=["CUSTOMER", "ORDERS"])

    # Example 5: Get a specific operation by ID
    #get_operation_by_id_example(76030)

    # Example 6: Get recent operations for a datastore
    # get_recent_operations_example(datastore_id=1734, size=10)

    # Example 7: Get all finished operations
    # get_recent_operations_example(finished=True, size=20)

    # Example 8: Abort a running operation
    # abort_operation_example(76042)

    print("\nPlease uncomment one of the example function calls above to run.")
