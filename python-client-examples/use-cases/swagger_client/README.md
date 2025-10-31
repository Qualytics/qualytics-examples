# swagger-client
Qualytics API

This Python package contains API client code generated from the Qualytics OpenAPI specification. The client includes:
- Models generated with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) (newer Pydantic models)
- Models generated with [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) (legacy models)
- Custom API client wrapper for compatibility

- API version: 5ca80d8 / 20251024-3d1ade3
- Package version: 1.0.0


## Updating this client

The client generation process has been updated to use modern tooling and includes a preprocessing step to fix naming issues in the OpenAPI specification.

### Prerequisites

1. Install OpenAPI Generator CLI (community fork of Swagger Codegen):
   ```bash
   npm install -g @openapitools/openapi-generator-cli
   ```

2. Ensure you have Python 3.7+ installed with `requests`:
   ```bash
   pip install requests
   ```

### Update Process

#### Step 1: Download the OpenAPI Specification

Download the OpenAPI spec from your Qualytics instance:

```bash
# Replace with your instance URL
curl https://your-instance.qualytics.io/api/openapi.json -o /tmp/qualytics-openapi.json
```

#### Step 2: Fix Long Schema Names

Before generating the client, you need to fix schema names that would create filenames longer than 255 characters. Use the `fix_openapi_spec.py` script located in the repository root:

```bash
cd /path/to/qualytics-examples
python fix_openapi_spec.py
```

This script:
- Reads the spec from `/tmp/qualytics-openapi.json`
- Identifies schema names that would create filenames > 240 characters
- Shortens long names using a hash-based approach (e.g., `VeryLongSchemaName...` → `VeryLongSchemaName_a1b2c3d4`)
- Updates all `$ref` references throughout the spec
- Saves the fixed spec to `/tmp/qualytics-openapi-fixed.json`

The script is located at: `fix_openapi_spec.py` (repository root)

#### Step 3: Validate the Fixed Specification (Optional)

You can validate the fixed spec using the OpenAPI Generator's validate command:

```bash
openapi-generator-cli validate -i /tmp/qualytics-openapi-fixed.json
```

Note: Some validation warnings are expected and won't prevent generation.

#### Step 4: Generate the Python Client

Generate the Python client using OpenAPI Generator:

```bash
openapi-generator-cli generate \
  -i /tmp/qualytics-openapi-fixed.json \
  -g python \
  -o ./swagger_client_new \
  --additional-properties=packageName=swagger_client,projectName=swagger_client
```

This generates a modern Python client with Pydantic models. The generator is the community-driven fork of the original Swagger Codegen and produces higher-quality code.

#### Step 5: Merge the Generated Code

1. Copy the new models from `swagger_client_new/models/` to this directory's `models/`
2. Copy the new API classes from `swagger_client_new/api/` to this directory's `api/`
3. **DO NOT replace** the `configuration.py` file - the version in this directory reads environment settings from the `.env` file
4. **DO NOT replace** the `custom_api_client.py` file - this provides lenient deserialization for compatibility

#### Step 6: Test the Updated Client

Run the example scripts to verify the client works:

```bash
cd ../quality_checks
python get_quality_checks.py

cd ../notifications
python get_user_notifications.py
```

## Custom Files (Do Not Replace)

The following files have been customized and should NOT be replaced during updates:

- **`configuration.py`** - Modified to read from `.env` file for API credentials
- **`custom_api_client.py`** - Provides lenient deserialization for mixed model types (Pydantic + legacy Swagger)
- **`__init__.py`** - May have custom imports

## Architecture Notes

This client contains a **hybrid model structure** due to multiple generations over time:
- **Pydantic models** (modern): Generated with OpenAPI Generator (community fork), used for newer API endpoints
- **Legacy Swagger models**: Generated with the original Swagger Codegen, used for older API endpoints
- **CustomApiClient**: Handles both model types gracefully with lenient deserialization

OpenAPI Generator is the actively maintained community fork of Swagger Codegen, providing better support for modern OpenAPI 3.x specifications and generating cleaner Python code with Pydantic models.

When the API response doesn't match the model validation (common with legacy models), the `CustomApiClient` catches the error and returns raw JSON data instead of raising an exception.

## Troubleshooting

### Deserialization Errors

If you see errors like `ValueError: Invalid value for X, must not be None`:
- This is expected for some endpoints with legacy models
- The `CustomApiClient` automatically handles this by returning dict instead of model objects
- Examples using `CustomApiClient` are in the `use-cases/` directories

### Import Errors

If models fail to import:
- Check that both old and new model files exist in `models/`
- Some models may have been renamed during the fix process
- Update imports in your code to match the new names

### API Credential Issues

The `configuration.py` reads from a `.env` file in the parent directory. Required variables:
```bash
API_BASE_URL=https://your-instance.qualytics.io
API_TOKEN=your-api-token
```

## Developer Guide: Creating New Use-Case Examples

This section explains how to create new example scripts in the `use-cases/` directories.

### File Structure Template

When creating a new example file (e.g., `update_anomaly.py` in `use-cases/anomalies/`), follow this structure:

```python
"""
Example script demonstrating how to [ACTION] using the Qualytics API swagger client.

Brief description of what this example does and any special considerations.

This example uses [old-style Swagger models / Pydantic models] since the [ENTITY] models
were generated with [Swagger Codegen / OpenAPI Generator]. The CustomApiClient is used to
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

# Configure API client with credentials from .env file
# The configuration reads API_TOKEN (Personal Access Token) and API_BASE_URL from the environment
configuration = swagger_client.Configuration()

# Create an instance of the API class using CustomApiClient
# The CustomApiClient handles lenient deserialization to avoid validation errors
api_instance = swagger_client.SomeApi(CustomApiClient(configuration))


def your_example_function():
    """
    Description of what this function does.

    Args:
        param1: Description
        param2: Description

    Returns:
        Description of return value
    """
    try:
        # Call the API
        api_response = api_instance.some_method(...)

        print("Success!")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print(f"Exception when calling Api->method: {e}\n")
        return None


if __name__ == '__main__':
    # Example usage
    your_example_function()
```

### Step-by-Step Guide

#### 1. Choose the Right Model Type

Determine whether your endpoint uses **Pydantic models** (new) or **old Swagger models**:

**Check the model file:**
```bash
# Pydantic models import from pydantic
grep "from pydantic import" swagger_client/models/your_model.py

# Old Swagger models have swagger_types
grep "swagger_types" swagger_client/models/your_model.py
```

**Pydantic Model Indicators:**
- File contains `from pydantic import BaseModel`
- Uses `model_dump()` or `dict()` methods
- Has type hints with `Optional`, `List`, etc.

**Old Swagger Model Indicators:**
- File contains `swagger_types` dictionary
- File contains `attribute_map` dictionary
- Generated by older Swagger Codegen

#### 2. Import Required Components

**Standard imports for all examples:**
```python
import sys
import os
from pprint import pprint

# Path setup - ALWAYS include this
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.custom_api_client import CustomApiClient
```

**Import specific models (if needed):**
```python
# For Pydantic models
from swagger_client.models.update_anomaly import UpdateAnomaly

# For old Swagger models
import swagger_client.models  # Access via swagger_client.ModelName
```

#### 3. Initialize the API Client

**Always use CustomApiClient** to avoid deserialization errors:

```python
# Configure API client
configuration = swagger_client.Configuration()

# Create API instance with CustomApiClient
api_instance = swagger_client.AnomaliesApi(CustomApiClient(configuration))
```

**Available API classes:**
- `AnomaliesApi` - Anomaly operations
- `ContainersApi` - Container operations
- `DatastoresApi` - Datastore operations
- `OperationsApi` - Operation scheduling and execution
- `QualityChecksApi` - Quality check management
- `NotificationsApi` - Notification management

#### 4. Build API Payloads

**Option A: Using Pydantic Models (Recommended for new endpoints)**

```python
from swagger_client.models.update_anomaly import UpdateAnomaly

# Create the model instance
payload = UpdateAnomaly(
    status="acknowledged",
    tags=["reviewed", "false-positive"]
)

# Pass to API method
api_response = api_instance.update_anomaly(id=anomaly_id, body=payload)
```

**Option B: Using Plain Dictionaries (Works with both model types)**

```python
# Build a dictionary matching the API schema
payload = {
    "status": "acknowledged",
    "tags": ["reviewed", "false-positive"]
}

# Pass to API method
api_response = api_instance.update_anomaly(id=anomaly_id, body=payload)
```

**Option C: Using Old Swagger Models**

```python
# Create the old-style model instance
payload = swagger_client.UpdateAnomaly(
    status="acknowledged",
    tags=["reviewed", "false-positive"]
)

# Pass to API method
api_response = api_instance.update_anomaly(id=anomaly_id, body=payload)
```

#### 5. Handle API Responses

Responses may be **objects** or **dicts** depending on whether deserialization succeeded:

```python
try:
    api_response = api_instance.some_method(...)

    # Handle both dict and object responses
    if isinstance(api_response, dict):
        # Deserialization failed, got raw dict
        items = api_response.get('items', [])
        total = api_response.get('total', 0)
    else:
        # Got model object
        items = api_response.items if hasattr(api_response, 'items') else []
        total = api_response.total if hasattr(api_response, 'total') else 0

    print(f"Retrieved {len(items)} items (total: {total})")
    pprint(api_response)
    return api_response

except ApiException as e:
    print(f"Exception when calling Api->method: {e}\n")
    return None
```

#### 6. Handle Paginated Responses

Many endpoints return paginated results:

```python
def get_paginated_example(page=1, size=50):
    """Get paginated results."""
    try:
        api_response = api_instance.get_items(page=page, size=size)

        # Handle paginated response
        if isinstance(api_response, dict):
            items = api_response.get('items', [])
            total = api_response.get('total', 0)
            current_page = api_response.get('page', page)
            pages = api_response.get('pages', 0)

            print(f"Page {current_page} of {pages} (total: {total})")
            print(f"Retrieved {len(items)} item(s) on this page")

            return items

        return api_response
    except ApiException as e:
        print(f"Error: {e}")
        return None
```

#### 7. Structure with Multiple Functions

Create helper functions for different use cases:

```python
def update_anomaly_status_example(anomaly_id, status):
    """Update anomaly status."""
    payload = {"status": status}

    try:
        api_response = api_instance.update_anomaly(id=anomaly_id, body=payload)
        print(f"Updated anomaly {anomaly_id} to status: {status}")
        return api_response
    except ApiException as e:
        print(f"Error: {e}")
        return None


def add_anomaly_tags_example(anomaly_id, tags):
    """Add tags to an anomaly."""
    payload = {"tags": tags}

    try:
        api_response = api_instance.update_anomaly(id=anomaly_id, body=payload)
        print(f"Added tags {tags} to anomaly {anomaly_id}")
        return api_response
    except ApiException as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    ANOMALY_ID = 12345  # Replace with actual ID

    # Uncomment the example you want to run:

    # Example 1: Update status
    # update_anomaly_status_example(ANOMALY_ID, "acknowledged")

    # Example 2: Add tags
    # add_anomaly_tags_example(ANOMALY_ID, ["reviewed", "expected"])

    print("Update ANOMALY_ID and uncomment an example to run.")
```

### Finding API Methods and Parameters

#### View Available API Methods

Check the API class file to see available methods:

```bash
# Example: View AnomaliesApi methods
grep "def " swagger_client/api/anomalies_api.py | grep -v "_with_http_info" | head -20
```

#### View Method Signatures

Look at the method definition in the API file:

```python
def update_anomaly(self, id, body, **kwargs):  # noqa: E501
    """Update Anomaly

    :param id: Anomaly ID (required)
    :param body: UpdateAnomaly (required)
    :return: GetAnomaly
    """
```

#### Check API Documentation

Refer to the official API docs for schema details:
```
https://your-instance.qualytics.io/api/docs
```

Or use the demo instance:
```
https://demo.qualytics.io/api/docs
```

### Best Practices

1. **Prefer Pydantic models** - but use CustomApi when needed
2. **Handle both dict and object responses** - deserialization may fail
3. **Use try/except blocks** around all API calls
4. **Provide clear docstrings** explaining what each function does
5. **Include multiple examples** in the `if __name__ == '__main__'` block
6. **Comment out example calls** by default so users must configure IDs
7. **Add helpful print statements** to show what's happening
8. **Use pprint** for displaying API responses
9. **Follow the existing file structure** in the use-cases directories
10. **Test your example** before committing

### Common Patterns

#### Creating a Resource
```python
def create_example():
    data = {
        "name": "My Resource",
        "description": "Description here"
    }

    try:
        api_response = api_instance.create_resource(body=data)
        print("Created successfully!")
        print(f"ID: {api_response.id if hasattr(api_response, 'id') else api_response.get('id')}")
        return api_response
    except ApiException as e:
        print(f"Error creating resource: {e}")
        return None
```

#### Updating a Resource
```python
def update_example(resource_id, **updates):
    try:
        api_response = api_instance.update_resource(id=resource_id, body=updates)
        print(f"Updated resource {resource_id}")
        return api_response
    except ApiException as e:
        print(f"Error updating resource: {e}")
        return None
```

#### Deleting a Resource
```python
def delete_example(resource_id):
    try:
        api_response = api_instance.delete_resource(id=resource_id)
        print(f"Deleted resource {resource_id}")
        return api_response
    except ApiException as e:
        print(f"Error deleting resource: {e}")
        return None
```

#### Listing Resources with Filters
```python
def list_example(filter_param=None, page=1, size=50):
    try:
        params = {'page': page, 'size': size}
        if filter_param:
            params['filter'] = filter_param

        api_response = api_instance.list_resources(**params)

        # Handle paginated response
        if isinstance(api_response, dict):
            items = api_response.get('items', [])
            print(f"Found {len(items)} resources")
            return items

        return api_response
    except ApiException as e:
        print(f"Error listing resources: {e}")
        return None
```

