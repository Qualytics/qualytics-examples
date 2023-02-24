import requests
import json

# Define the base URL for the API
AUTH_URL = "auth.qualytics.io"
BASE_URL = "YOUR_DEPLOYMENT_URL" # ex: https://acme.qualytics.io/api

# Secrets for Auth Token
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_SECRET"


# Start Helper functions
def _get_token():
    audience = "brookfield-api"
    grant_type = "client_credentials"

    # Define the endpoint for token retrieval
    url = f"https://{AUTH_URL}/oauth/token"

    # Define the request body data
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": audience,
        "grant_type": grant_type
    }

    # Make the request
    response = requests.post(url, json=data)

    # Extract and return the token from the response
    token = response.json()["access_token"]

    return token


def _get_default_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }


def _pprint(text):
    print(json.dumps(json.loads(text), indent=2))


# End Helper functions

# Start API functions
def get_datastores(token):
    # Define the full URL for the endpoint
    endpoint = "datastores"
    url = f"{BASE_URL}/{endpoint}"

    # Define parameters for the endpoint
    params = {"sort_created": "desc"}

    # Make the request
    response = requests.get(url, headers=_get_default_headers(token), params=params)

    # Print the response content
    _pprint(response.content)


def get_datastore_by_id(token, id):
    # Define the full URL for the endpoint
    endpoint = "datastores"
    url = f"{BASE_URL}/{endpoint}/{id}"

    # Make the request
    response = requests.get(url, headers=_get_default_headers(token))

    # Print the response content
    _pprint(response.content)


def get_datastore_containers(token, datastore_id):
    # Define the full URL for the endpoint
    endpoint = "containers"
    url = f"{BASE_URL}/{endpoint}"

    # Define parameters for the endpoint
    params = {"datastore": datastore_id, "sort_name": "asc"}

    # Make the request
    response = requests.get(url, headers=_get_default_headers(token), params=params)

    # Print the response content
    _pprint(response.content)


# End API functions

# Main
def main():
    token = _get_token()

    get_datastores(token)
    # get_datastore_by_id(token, 162) # uncomment this line to get the datastore by id
    # get_datastore_containers(token, 162) # uncomment this line to get the datastore containers


if __name__ == '__main__':
    main()