
import requests
import json

# Define the base URL for the API
BASE_URL = "https://develop.qualytics.io/api"
#"YOUR_DEPLOYMENT_URL" # ex: https://acme.qualytics.io/api

# Secrets for Auth Token
PERSONAL_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGQiOnsiaWQiOiJnb29nbGUtYXBwc3xndXN0YXZvQHF1YWx5dGljcy5jbyIsImVtYWlsIjoiZ3VzdGF2b0BxdWFseXRpY3MuY28iLCJuYW1lIjoiR3VzdGF2byBDYXJkb3NvIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BTFYtVWpXSzA3TWJVZ1kwTjRBRHlSRk5HTkRlTzRvcUhvSHJyMmFBMW84YlFGWnNuWU1FeVRZZDRkRkhZOFlBV0dUb0czLWtWQmxRWFY0bkJGZmQ2bENlTGY5eUJvSTlNYlphTWxqWk1fYzJnYU95cFdHSHdXOE1USXhoUHAzaWFuRW1sQmhqT1FoTWh2S2JlMGstcDgzU293SG5hSDRQWGVGNnhoZThhQ3hXMnVJRVhYZm50S2did1gwbmRSaDZyd0NIVHU4VmNfWEJ0WkdldHJlN2pfWWRUUzBKOWpaY20zUnZsaEFJU3pqd0pxN0ExcE5fRy1ER3BSaTE3ZkMySzVjY25zNU5HRmp0dzBwQUNDNVkxS1BudkREVVRrZ2ViUjlpRjQxdzRlTjh5T3FVNTNnUkFac01mOFdTSExqazhRdmVnM2t0UF9OX2ZYSjdBYmlpSXVRQ0lDMENRWkg5eDJJYWhGVENqTVVuUXZhUUVFblU1SGxJanZrWDQ5dEFFZFhGVlVZWm9yaFhhVVhaWkp1LWJFZnVUMVJpaHJqdUtraXlMQXExR2VtVE04ZmZTZkE3WVZOTDY5SThUd3NZOEYyWGMwYmFra3Zmcmhja2IzMlpwMFBVMTAyY1hMZFJqU3Rnamk2eXk4bDYxdG9wSm5zeGc5MlR0QjJZS1RGcExkWjNCUXdUWGZmeTFuMFNKbDBncFd6dU5IanRkZHJ3OWgzUTZacmR5MGZWMWprbG43dnB3cXRvUTRpQXVLWExuMlZEdC1HZTJsWWhyQk9DQU1qNzJKd1FsWEZCX2ItYVBCNDJqNF8xc0xyVl96YnZ2RWNRNnFOeWZSN2Nmd1YyMkpQal9UQjZyMVFzU2ppUVhaWDYwQnZvZmV2SGNBcVROelZwOVV2eGFEZXRfZ1dMQWlUczZLMU50M0xlVGlEZ3pYYldDR0pnSS1yeTBEY0cxOFZ4T2pxOTlsMnJWSFR0YmdqUEZTUzlwcWdTTUJGNlR2YnBnUzkxR1hZWFFpMTlNSFdXRGduZDZxajFOaXk2LTFnQzhkdHBBZzFkRHpoeTl0UWV1MktCMHBydjlRQk1XZVdxbXBlSW82NF9scTd5S2pkdExfUXZyZDBobEx6YVYyakZNUV9KTmNUaXlaaTVGMVBaWHdEbnUwUVVMVXd2ZThwRDBJZmxMUEw1S2NuZThRRnFISmRjbTl3bEg5djJVeUhvRG83V2Zrcjc0OU1WdDc0QXRTemhscVVXNHJUVFNVRE1UWnNVQWpRb0xnWlJSdzBTU1VSUkpxdjg1d3BhdUstdjM0T2VSckMxT0d4d2tKS2ZIclBxZlMwLVczUVRtLWxWPXM5Ni1jIiwic2NpbV9yZXN0cmljdGVkIjpmYWxzZX0sInN1YiI6Imdvb2dsZS1hcHBzfGd1c3Rhdm9AcXVhbHl0aWNzLmNvIiwiaXNzIjoiaHR0cHM6Ly9xdWFseXRpY3MuaW8iLCJjcnQiOiIyMDI1LTEwLTE0VDE1OjU0OjAxLjk0NzIwOSswMDowMCIsImV4cCI6MTc2MzA0OTI0MX0.lOzgbMTR94MnFYY6d-s4DSYckk5xjMYZgE7x7Fg1eMo"
# "YOUR_TOKEN_HERE"


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