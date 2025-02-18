import requests
import json

# Define the base URL for the API
AUTH_URL = "auth.qualytics.io"
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
def get_datastores():
    # Define the full URL for the endpoint
    endpoint = "datastores"
    url = f"{BASE_URL}/{endpoint}"

    # Define parameters for the endpoint
    params = {"sort_created": "desc"}

    # Make the request
    response = requests.get(url, headers=_get_default_headers(), params=params)

    # Print the response content
    _pprint(response.content)


def get_datastore_by_id(id):
    # Define the full URL for the endpoint
    endpoint = "datastores"
    url = f"{BASE_URL}/{endpoint}/{id}"

    # Make the request
    response = requests.get(url, headers=_get_default_headers())

    # Print the response content
    _pprint(response.content)


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


# End API functions

# Main
def main():
    # get_datastores() # uncomment this line to get the datastores
    # get_datastore_by_id(844) # uncomment this line to get the datastore by id
    get_datastore_containers(844)


if __name__ == '__main__':
    main()