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

    # Example 4: Update a container - add tags
    # update_container(
    #     container_id=43664,
    #     container_type="table",
    #     tags=["B2B"]
    # )

    # Uncomment one of the examples above to run
    print("Please uncomment one of the example function calls in main() to run")


if __name__ == '__main__':
    main()