#!/usr/bin/env python3
"""
Script to fix naming issues in the Qualytics OpenAPI specification.

This script:
1. Downloads the OpenAPI spec from the Qualytics API
2. Fixes problematic model names that cause generation issues
3. Saves the fixed spec for client generation

The main issues this script addresses:
- Model names with special characters (dots, dashes, spaces)
- Names that are Python reserved keywords
- Overly long or complex generated names
- Inconsistent naming patterns

Usage:
    python fix_openapi_spec.py [--url https://your-instance.qualytics.io] [--output openapi_fixed.json]

Examples:
    # Use default demo instance
    python fix_openapi_spec.py

    # Use your own instance
    python fix_openapi_spec.py --url https://acme.qualytics.io

    # Specify custom output file
    python fix_openapi_spec.py --url https://acme.qualytics.io --output my_spec.json
"""

import requests
import json
import re
import sys
from typing import Dict, Any, Set


def fix_model_names(spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Fix problematic model names in the OpenAPI spec.

    Args:
        spec: The OpenAPI specification dictionary

    Returns:
        The modified specification with fixed model names
    """
    if 'components' not in spec or 'schemas' not in spec['components']:
        print("Warning: No component schemas found in spec")
        return spec

    schemas = spec['components']['schemas']
    fixes = {}

    # Python reserved keywords that need to be avoided
    reserved_keywords = {
        'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
        'elif', 'else', 'except', 'False', 'finally', 'for', 'from', 'global',
        'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or',
        'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield'
    }

    print(f"\nAnalyzing {len(schemas)} schemas for naming issues...")

    for name, schema in schemas.items():
        new_name = name
        reasons = []

        # Fix 1: Replace special characters with underscores
        if re.search(r'[.\-\s]+', name):
            new_name = re.sub(r'[.\-\s]+', '_', new_name)
            reasons.append("special characters")

        # Fix 2: Handle Python reserved keywords
        if new_name.lower() in reserved_keywords:
            new_name = f"{new_name}_Model"
            reasons.append("reserved keyword")

        # Fix 3: Ensure names start with a letter
        if new_name and not new_name[0].isalpha():
            new_name = f"Model_{new_name}"
            reasons.append("starts with non-letter")

        # Fix 4: Remove any remaining invalid characters
        if re.search(r'[^\w]', new_name):
            new_name = re.sub(r'[^\w]', '_', new_name)
            reasons.append("invalid characters")

        # Fix 5: Remove consecutive underscores
        if '__' in new_name:
            new_name = re.sub(r'_+', '_', new_name)
            reasons.append("consecutive underscores")

        # Fix 6: Remove leading/trailing underscores
        new_name = new_name.strip('_')

        # Record the fix if name changed
        if new_name != name:
            fixes[name] = (new_name, reasons)

    # Apply fixes to schemas
    print(f"\nApplying {len(fixes)} naming fixes...")
    for old_name, (new_name, reasons) in fixes.items():
        schemas[new_name] = schemas.pop(old_name)
        print(f"  ✓ {old_name} -> {new_name} ({', '.join(reasons)})")

    # Update references to renamed schemas throughout the spec
    if fixes:
        print("\nUpdating schema references...")
        spec_str = json.dumps(spec)
        for old_name, (new_name, _) in fixes.items():
            # Update $ref references
            old_ref = f'"#/components/schemas/{old_name}"'
            new_ref = f'"#/components/schemas/{new_name}"'
            spec_str = spec_str.replace(old_ref, new_ref)

        spec = json.loads(spec_str)
        print(f"  ✓ Updated {len(fixes)} schema references")

    return spec


def download_and_fix_spec(api_url: str, output_file: str) -> bool:
    """
    Download the OpenAPI spec from Qualytics API and apply fixes.

    Args:
        api_url: Base URL of the Qualytics instance
        output_file: Path where the fixed spec should be saved

    Returns:
        True if successful, False otherwise
    """
    openapi_url = f"{api_url}/api/openapi.json"
    print(f"Downloading OpenAPI spec from {openapi_url}...")

    try:
        response = requests.get(openapi_url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading spec: {e}")
        return False

    try:
        spec = response.json()
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON spec: {e}")
        return False

    # Display spec info
    info = spec.get('info', {})
    print(f"  ✓ Downloaded spec")
    print(f"    Title: {info.get('title', 'Unknown')}")
    print(f"    Version: {info.get('version', 'Unknown')}")

    # Count endpoints
    paths_count = len(spec.get('paths', {}))
    schemas_count = len(spec.get('components', {}).get('schemas', {}))
    print(f"    Paths: {paths_count}")
    print(f"    Schemas: {schemas_count}")

    # Apply fixes
    print("\n" + "="*60)
    print("Applying fixes...")
    print("="*60)
    fixed_spec = fix_model_names(spec)

    # Save the fixed spec
    print(f"\nSaving fixed spec to {output_file}...")
    try:
        with open(output_file, 'w') as f:
            json.dump(fixed_spec, f, indent=2)
        print(f"  ✓ Fixed spec saved successfully")
        return True
    except IOError as e:
        print(f"Error saving fixed spec: {e}")
        return False


def main():
    """Main entry point for the script."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Fix Qualytics OpenAPI specification for Python client generation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default demo instance
  %(prog)s

  # Use your own instance
  %(prog)s --url https://acme.qualytics.io

  # Specify custom output file
  %(prog)s --url https://acme.qualytics.io --output my_spec.json
        """
    )

    parser.add_argument(
        '--url',
        default='https://demo.qualytics.io',
        help='Qualytics instance URL (default: https://demo.qualytics.io)'
    )
    parser.add_argument(
        '--output',
        default='openapi_fixed.json',
        help='Output file for fixed spec (default: openapi_fixed.json)'
    )

    args = parser.parse_args()

    print("="*60)
    print("Qualytics OpenAPI Spec Fixer")
    print("="*60)

    success = download_and_fix_spec(args.url, args.output)

    print("\n" + "="*60)
    if success:
        print("✓ SUCCESS")
        print("="*60)
        print(f"\nFixed specification saved to: {args.output}")
        print("\nNext steps:")
        print("  1. Validate: openapi lint", args.output)
        print("  2. Generate client: openapi-generator-cli generate ...")
        print("\nSee swagger_client/README.md for detailed instructions.")
        return 0
    else:
        print("✗ FAILED")
        print("="*60)
        print("\nThe spec could not be fixed. Check the errors above.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
