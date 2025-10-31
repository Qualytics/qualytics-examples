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

