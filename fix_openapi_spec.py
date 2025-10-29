#!/usr/bin/env python3
"""
Script to fix OpenAPI spec by shortening schema names that would cause
filenames longer than 255 characters when generating Python client.
"""
import json
import hashlib

def shorten_name(name, max_length=200):
    """Shorten a schema name if it's too long."""
    if len(name) <= max_length:
        return name

    # Create a shortened version with hash
    # Keep first 150 chars and add hash of full name
    name_hash = hashlib.md5(name.encode()).hexdigest()[:8]
    shortened = name[:150] + "_" + name_hash
    return shortened

def update_references(obj, name_mapping):
    """Recursively update all $ref references in the spec."""
    if isinstance(obj, dict):
        if '$ref' in obj:
            ref = obj['$ref']
            if ref.startswith('#/components/schemas/'):
                schema_name = ref.replace('#/components/schemas/', '')
                if schema_name in name_mapping:
                    obj['$ref'] = f'#/components/schemas/{name_mapping[schema_name]}'

        for key, value in obj.items():
            update_references(value, name_mapping)

    elif isinstance(obj, list):
        for item in obj:
            update_references(item, name_mapping)

# Load the OpenAPI spec
with open('/tmp/qualytics-openapi.json', 'r') as f:
    spec = json.load(f)

# Find and map long schema names
schemas = spec.get('components', {}).get('schemas', {})
name_mapping = {}

print("Analyzing schema names...")
long_names = []

for name in schemas.keys():
    # Estimate filename length (Python generator adds .py and converts to snake_case)
    # Conservative estimate: name might be slightly longer in snake_case
    estimated_filename_length = len(name) + 10

    if estimated_filename_length > 240:  # Leave margin for safety
        short_name = shorten_name(name)
        name_mapping[name] = short_name
        long_names.append((name, short_name, estimated_filename_length))
        print(f"  {name[:80]}... ({estimated_filename_length} chars) -> {short_name}")

print(f"\nFound {len(long_names)} schema names to shorten")

# Rename schemas
if name_mapping:
    new_schemas = {}
    for old_name, schema_def in schemas.items():
        new_name = name_mapping.get(old_name, old_name)
        new_schemas[new_name] = schema_def

    spec['components']['schemas'] = new_schemas

    # Update all references throughout the spec
    print("\nUpdating references throughout the spec...")
    update_references(spec, name_mapping)

# Save the fixed spec
output_file = '/tmp/qualytics-openapi-fixed.json'
with open(output_file, 'w') as f:
    json.dump(spec, f, indent=2)

print(f"\nFixed OpenAPI spec saved to: {output_file}")
print(f"Shortened {len(name_mapping)} schema names")
