"""
Example script demonstrating how to create and manage scheduled operations using the Qualytics API swagger client.

This example shows how to schedule different types of operations (catalog, profile, scan) using cron syntax,
as well as how to retrieve, update, and delete scheduled operations.

This example uses old-style Swagger models since the operation models were generated with
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
api_instance = swagger_client.OperationsApi(CustomApiClient(configuration))


def create_schedule_operation_example(operation_type, datastore_id, crontab, **kwargs):
    """
    Create a scheduled operation.

    Args:
        operation_type (str): Type of operation - 'catalog', 'profile', or 'scan'
        datastore_id (int): The ID of the datastore to run the operation on
        crontab (str): Cron expression for scheduling (e.g., "*/10 * * * *" for every 10 minutes)
        **kwargs: Additional operation-specific parameters

    Returns:
        The created scheduled operation details

    Cron expression format: minute hour day month day_of_week
    Examples:
        - "0 2 * * *"       - Every day at 2:00 AM
        - "*/15 * * * *"    - Every 15 minutes
        - "0 9 * * 1-5"     - 9:00 AM on weekdays
        - "0 0 1 * *"       - First day of every month at midnight
    """
    # Prepare the schedule operation data
    # See the official docs for the expected schema and valid values:
    # https://demo.qualytics.io/api/docs#tag/operations/operation/create_schedule_operation
    data = {
        "type": operation_type,
        "datastore_id": datastore_id,
        "crontab": crontab,
    }

    # Add any additional parameters
    data.update(kwargs)

    try:
        # Create the scheduled operation
        api_response = api_instance.create_schedule_operation(data)

        print(f"Scheduled {operation_type} operation created successfully!")
        print(f"Schedule: {crontab}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->create_schedule_operation: %s\n" % e)
        return None


def create_scheduled_catalog_example(datastore_id, crontab="0 2 * * *"):
    """
    Create a scheduled catalog operation.

    Catalog operations discover and register data containers (tables/files) in a datastore.

    Args:
        datastore_id (int): The ID of the datastore
        crontab (str): Cron expression (default: daily at 2 AM)

    Returns:
        The created scheduled operation
    """
    print(f"\n=== Creating scheduled catalog operation ===")
    return create_schedule_operation_example(
        operation_type="catalog",
        datastore_id=datastore_id,
        crontab=crontab
    )


def create_scheduled_profile_example(datastore_id, crontab="0 3 * * *", infer_constraints=True):
    """
    Create a scheduled profile operation.

    Profile operations analyze data patterns and optionally infer quality check constraints.

    Args:
        datastore_id (int): The ID of the datastore
        crontab (str): Cron expression (default: daily at 3 AM)
        infer_constraints (bool): Whether to infer quality check constraints (default: True)

    Returns:
        The created scheduled operation
    """
    print(f"\n=== Creating scheduled profile operation ===")
    return create_schedule_operation_example(
        operation_type="profile",
        datastore_id=datastore_id,
        crontab=crontab,
        infer_constraints=infer_constraints
    )


def create_scheduled_scan_example(datastore_id, crontab="*/30 * * * *", incremental=True):
    """
    Create a scheduled scan operation.

    Scan operations check data quality against defined quality checks.

    Args:
        datastore_id (int): The ID of the datastore
        crontab (str): Cron expression (default: every 30 minutes)
        incremental (bool): Whether to scan only new/changed data (default: True)

    Returns:
        The created scheduled operation
    """
    print(f"\n=== Creating scheduled scan operation ===")
    return create_schedule_operation_example(
        operation_type="scan",
        datastore_id=datastore_id,
        crontab=crontab,
        incremental=incremental
    )


def get_scheduled_operations_example(datastore_id=None, operation_type=None):
    """
    Get a list of scheduled operations with optional filters.

    Args:
        datastore_id (int): Optional - filter by datastore ID
        operation_type (str): Optional - filter by operation type ('catalog', 'profile', 'scan')

    Returns:
        List of scheduled operations
    """
    try:
        params = {}
        if datastore_id is not None:
            params['datastore'] = datastore_id
        if operation_type is not None:
            params['type'] = operation_type

        api_response = api_instance.get_scheduled_operations(**params)

        # Handle response - could be a list or paginated response
        if isinstance(api_response, dict):
            items = api_response.get('items', api_response)
            print(f"\nRetrieved {len(items)} scheduled operation(s)")
            pprint(items)
        elif isinstance(api_response, list):
            print(f"\nRetrieved {len(api_response)} scheduled operation(s)")
            pprint(api_response)
        else:
            print("\nRetrieved scheduled operations:")
            pprint(api_response)

        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->get_scheduled_operations: %s\n" % e)
        return None


def get_scheduled_operation_by_id_example(schedule_id):
    """
    Get details of a specific scheduled operation.

    Args:
        schedule_id (int): The ID of the scheduled operation

    Returns:
        The scheduled operation details
    """
    try:
        api_response = api_instance.get_scheduled_operation(id=schedule_id)

        print(f"\nRetrieved scheduled operation {schedule_id}:")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->get_scheduled_operation: %s\n" % e)
        return None


def update_scheduled_operation_example(schedule_id, crontab=None, **kwargs):
    """
    Update a scheduled operation.

    Args:
        schedule_id (int): The ID of the scheduled operation to update
        crontab (str): Optional - new cron expression
        **kwargs: Additional parameters to update

    Returns:
        The updated scheduled operation
    """
    try:
        # Build update data
        data = {}
        if crontab:
            data["crontab"] = crontab
        data.update(kwargs)

        api_response = api_instance.update_schedule_operation(body=data, id=schedule_id)

        print(f"\nScheduled operation {schedule_id} updated successfully!")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->update_schedule_operation: %s\n" % e)
        return None


def delete_scheduled_operation_example(schedule_id):
    """
    Delete a scheduled operation.

    Args:
        schedule_id (int): The ID of the scheduled operation to delete

    Returns:
        Confirmation of deletion
    """
    try:
        api_response = api_instance.delete_schedule_operation(id=schedule_id)

        print(f"\nScheduled operation {schedule_id} deleted successfully!")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OperationsApi->delete_schedule_operation: %s\n" % e)
        return None


if __name__ == '__main__':
    # Update these values with your actual IDs
    DATASTORE_ID = 1734  # Replace with your actual datastore ID
    SCHEDULE_ID = 0     # Replace with an actual schedule ID for update/delete examples

    # Uncomment the example you want to run:

    # Example 1: Create a scheduled catalog operation (daily at 2 AM)
    create_scheduled_catalog_example(DATASTORE_ID, crontab="0 2 * * *")

    # Example 2: Create a scheduled profile operation (daily at 3 AM with constraint inference)
    # create_scheduled_profile_example(DATASTORE_ID, crontab="0 3 * * *", infer_constraints=True)

    # Example 3: Create a scheduled scan operation (every 30 minutes, incremental)
    # create_scheduled_scan_example(DATASTORE_ID, crontab="*/30 * * * *", incremental=True)

    # Example 4: Create a scheduled scan operation (every hour)
    # create_scheduled_scan_example(DATASTORE_ID, crontab="0 * * * *", incremental=True)

    # Example 5: Get all scheduled operations
    # get_scheduled_operations_example()

    # Example 6: Get scheduled operations for a specific datastore
    # get_scheduled_operations_example(datastore_id=DATASTORE_ID)

    # Example 7: Get scheduled operations by type
    # get_scheduled_operations_example(operation_type="scan")

    # Example 8: Get a specific scheduled operation by ID
    # get_scheduled_operation_by_id_example(SCHEDULE_ID)

    # Example 9: Update a scheduled operation's cron schedule
    # update_scheduled_operation_example(SCHEDULE_ID, crontab="0 4 * * *")

    # Example 10: Delete a scheduled operation
    # delete_scheduled_operation_example(SCHEDULE_ID)

    print("\nPlease update DATASTORE_ID and uncomment one of the example function calls above to run.")
