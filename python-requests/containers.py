import requests
import json

# Define the base URL for the API
BASE_URL = "YOUR_DEPLOYMENT_URL" # ex: https://acme.qualytics.io/api

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
def get_datastore_containers(datastore_id):
    # Define the full URL for the endpoint
    endpoint = "containers"
    url = f"{BASE_URL}/{endpoint}"

    # Define parameters for the endpoint
    params = {"datastore": datastore_id, "sort_name": "asc"}

    # Make the request
    response = requests.get(url, headers=_get_default_headers(), params=params)

    # Print the response content
    _pprint(response.content)


def get_container_by_id(container_id):
    """
    Get details of a specific container by ID.

    Args:
        container_id (int): The ID of the container to retrieve
    """
    # Define the full URL for the endpoint
    endpoint = f"containers/{container_id}"
    url = f"{BASE_URL}/{endpoint}"

    # Make the request
    response = requests.get(url, headers=_get_default_headers())

    # Print the response content
    print(f"Status Code: {response.status_code}")
    _pprint(response.content)


def create_computed_table_container(datastore_id, name, query, additional_metadata=None):
    """
    Create a computed table container using a SQL query.
    Computed containers are virtual containers created from queries on existing containers.

    Args:
        datastore_id (int): The ID of the datastore where the computed table will be created
        name (str): The name of the computed table
        query (str): SQL query to create the computed table (e.g., "SELECT * FROM schema.table WHERE status='active'")
        additional_metadata (dict): Optional additional metadata for the computed table
    """
    # Define the full URL for the endpoint
    endpoint = "containers"
    url = f"{BASE_URL}/{endpoint}"

    # Define the request body for computed table container
    body = {
        "container_type": "computed_table",
        "datastore_id": datastore_id,
        "name": name,
        "query": query
    }

    # Add optional fields if provided
    if additional_metadata:
        body["additional_metadata"] = additional_metadata

    # Make the request
    response = requests.post(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Successfully created computed table container: {name}")
        _pprint(response.content)
    else:
        print(f"Failed to create computed table container: {response.text}")


def create_computed_file_container(datastore_id, source_container_id, name,
                                   select_clause, where_clause=None, additional_metadata=None):
    """
    Create a computed file container with transformations on an existing file container.

    Args:
        datastore_id (int): The ID of the datastore where the computed file will be created
        source_container_id (int): The ID of the source file container to transform
        name (str): The name of the computed file
        select_clause (str): SQL SELECT clause to transform the data (e.g., "col1, col2, UPPER(col3) as col3_upper")
        where_clause (str): Optional WHERE clause to filter data
        additional_metadata (dict): Optional additional metadata
    """
    # Define the full URL for the endpoint
    endpoint = "containers"
    url = f"{BASE_URL}/{endpoint}"

    # Define the request body for computed file container
    body = {
        "container_type": "computed_file",
        "datastore_id": datastore_id,
        "source_container_id": source_container_id,
        "name": name,
        "select_clause": select_clause
    }

    # Add optional fields if provided
    if where_clause:
        body["where_clause"] = where_clause
    if additional_metadata:
        body["additional_metadata"] = additional_metadata

    # Make the request
    response = requests.post(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Successfully created computed file container: {name}")
        _pprint(response.content)
    else:
        print(f"Failed to create computed file container: {response.text}")


def create_computed_join_container(name, left_container_id, left_join_field_name,
                                   right_container_id, right_join_field_name,
                                   select_clause, join_type="inner",
                                   left_prefix="left", right_prefix="right",
                                   where_clause=None, additional_metadata=None):
    """
    Create a computed join container by joining two existing containers.

    Args:
        name (str): The name of the joined container
        left_container_id (int): The container ID of the left side
        left_join_field_name (str): The field to join on from the left side
        right_container_id (int): The container ID of the right side
        right_join_field_name (str): The field to join on from the right side
        select_clause (str): SELECT clause using prefixed field names (e.g., "left.id, right.name")
        join_type (str): Type of join - "inner", "left", "right", or "full" (default: "inner")
        left_prefix (str): Alias prefix for left side columns (default: "left")
        right_prefix (str): Alias prefix for right side columns (default: "right")
        where_clause (str): Optional WHERE clause to filter the join result
        additional_metadata (dict): Optional additional metadata
    """
    # Define the full URL for the endpoint
    endpoint = "containers"
    url = f"{BASE_URL}/{endpoint}"

    # Define the request body for computed join container
    body = {
        "container_type": "computed_join",
        "name": name,
        "left_container_id": left_container_id,
        "left_join_field_name": left_join_field_name,
        "left_prefix": left_prefix,
        "right_container_id": right_container_id,
        "right_join_field_name": right_join_field_name,
        "right_prefix": right_prefix,
        "join_type": join_type,
        "select_clause": select_clause
    }

    # Add optional fields if provided
    if where_clause:
        body["where_clause"] = where_clause
    if additional_metadata:
        body["additional_metadata"] = additional_metadata

    # Make the request
    response = requests.post(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Successfully created computed join container: {name}")
        _pprint(response.content)
    else:
        print(f"Failed to create computed join container: {response.text}")


def update_container(container_id, container_type, exclude_fields=None, tags=None,
                     freshness_tracking_enabled=None, volumetric_tracking_enabled=None,
                     partition_field=None, incremental_field_name=None,
                     incremental_identifier_type=None, additional_metadata=None):
    """
    Update an existing container's configuration.

    Args:
        container_id (int): The ID of the container to update
        container_type (str): Type of container - 'table', 'file', 'computed_table', 'computed_file', 'computed_join'
        exclude_fields (list): List of field names to exclude from profiling/scanning
        tags (list): List of tags to apply to the container
        freshness_tracking_enabled (bool): Enable/disable freshness tracking
        volumetric_tracking_enabled (bool): Enable/disable volumetric tracking
        partition_field (str): Field name used for partitioning
        incremental_field_name (str): Field name for incremental scans
        incremental_identifier_type (str): Type - 'last-modified', 'batch-value', or 'postgresql'
        additional_metadata (dict): Additional metadata for the container
    """
    # Define the full URL for the endpoint
    endpoint = f"containers/{container_id}"
    url = f"{BASE_URL}/{endpoint}"

    # Define the request body - container_type is required
    body = {
        "container_type": container_type
    }

    # Add optional fields if provided
    if exclude_fields is not None:
        body["exclude_fields"] = exclude_fields
    if tags is not None:
        body["tags"] = tags
    if freshness_tracking_enabled is not None:
        body["freshness_tracking_enabled"] = freshness_tracking_enabled
    if volumetric_tracking_enabled is not None:
        body["volumetric_tracking_enabled"] = volumetric_tracking_enabled
    if partition_field is not None:
        body["partition_field"] = partition_field
    if incremental_field_name is not None:
        body["incremental_field_name"] = incremental_field_name
    if incremental_identifier_type is not None:
        body["incremental_identifier_type"] = incremental_identifier_type
    if additional_metadata is not None:
        body["additional_metadata"] = additional_metadata

    # Make the request
    response = requests.put(url, headers=_get_default_headers(), json=body)

    # Print the response content
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Successfully updated container {container_id}")
        _pprint(response.content)
    else:
        print(f"Failed to update container: {response.text}")


# End API functions

# Main
def main():

    # Example 1: Get all containers for a datastore
    # get_datastore_containers(844)

    # Example 2: Get a specific container by ID
    # get_container_by_id(28751)

    # Example 3: Create a computed table container (virtual table from SQL query)
    # create_computed_table_container(
    #     datastore_id=1734,
    #     name="active_nation",
    #     query="SELECT * FROM nation"
    # )

    # Example 6: Create a computed file container (transformed file container)
    # create_computed_file_container(
    #     datastore_id=1711,
    #     source_container_id=43664,  # ID of the source file container
    #     name="filtered_customer_data",
    #     select_clause="business_id",
    # )

    # Example 7: Create a computed join container (join two containers)
    # create_computed_join_container(
    #     name="customers_with_orders",
    #     left_container_id=1234,  # customers table
    #     left_join_field_name="customer_id",
    #     right_container_id=5678,  # orders table
    #     right_join_field_name="customer_id",
    #     select_clause="left.customer_id, left.name, left.email, right.order_id, right.order_total",
    #     join_type="inner"
    # )

    # Example 8: Update a container - add tags
    # update_container(
    #     container_id=43664,
    #     container_type="table",
    #     tags=["B2B"]
    # )

    # Uncomment one of the examples above to run
    print("Please uncomment one of the example function calls in main() to run")


if __name__ == '__main__':
    main()