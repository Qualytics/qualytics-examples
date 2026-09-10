#!/usr/bin/env python3
# =============================================================================
#  Qualytics API demo - create "Not Null" data quality checks in bulk
#
#  What this script does, in plain English:
#    1. Asks Qualytics: "what tables do you have in this datastore?"   (GET)
#    2. Asks Qualytics: "what columns does each table have?"           (GET)
#    3. Tells Qualytics: "create a Not Null check on each column"      (POST)
#
#  A "Not Null" check is the simplest data quality rule there is:
#  it flags any row where that column is empty.
# =============================================================================

# -----------------------------------------------------------------------------
#  STEP 1: Fill in these settings, save the file, then run:  python3 bulk_not_null_checks.py
# -----------------------------------------------------------------------------

BASE_URL = "https://your-instance.qualytics.io"  # your Qualytics web address
API_TOKEN = "paste-your-api-token-here"  # your API token (like a keycard)

DATASTORE_ID = 123  # the datastore to work in (the number in the URL when you open it)

TABLE_NAMES = []  # which tables to use, e.g. ["CUSTOMERS", "ORDERS"]
# leave it empty [] to use EVERY table in the datastore

# --- Values used for the develop-instance dry run (paste your own token): ----
# BASE_URL = "https://develop.qualytics.io"
# API_TOKEN = "<generate one in Settings -> Security -> API Keys>"
# DATASTORE_ID = 4314
# TABLE_NAMES = ["CRM_CUSTOMERS", "RECON_A_LEDGER"]

TAG_NAME = "API Demo"  # a label added to every check so they are easy to find
# (and easy to clean up later); set to None to skip tagging

MAX_CHECKS = 50  # safety limit - stop after creating this many checks

VERIFY_SSL = False  # set to False for on-prem installs that use their own
# (self-signed) HTTPS certificate; keep True for cloud instances

# -----------------------------------------------------------------------------
#  No changes needed below this line.
# -----------------------------------------------------------------------------

import sys

try:
    import requests  # the standard Python library for talking to web APIs
except ImportError:
    sys.exit("Please install the 'requests' package first:  pip3 install requests")

BASE_URL = BASE_URL.rstrip("/")

# Every request carries the token so Qualytics knows who we are.
HEADERS = {"Authorization": "Bearer " + API_TOKEN}

# When certificate verification is off, Python prints a warning on every
# single request - silence it so the demo output stays readable.
if not VERIFY_SSL:
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# =============================================================================
#  PART 1 - EXTRACT (GET): pull tables and columns out of Qualytics
# =============================================================================

print()
print("PART 1 - Reading tables and columns from datastore %s ..." % DATASTORE_ID)
print()

# --- 1a. Get the list of tables (Qualytics calls them "containers") ----------
#     GET /api/containers?datastore=<id>
response = requests.get(
    BASE_URL + "/api/containers",
    headers=HEADERS,
    params={"datastore": DATASTORE_ID, "size": 100},
    verify=VERIFY_SSL,
)
response.raise_for_status()  # stop with a clear error if something went wrong
tables = response.json()["items"]

# If specific table names were listed above, keep only those.
if TABLE_NAMES:
    wanted = [name.lower() for name in TABLE_NAMES]
    tables = [t for t in tables if t["name"].lower() in wanted]

if not tables:
    sys.exit("No tables found - double-check DATASTORE_ID and TABLE_NAMES.")

# --- 1b. For each table, get its columns (Qualytics calls them "fields") -----
#     GET /api/fields?container_id=<table id>
#
# We collect everything into one "payload": a simple list where each entry
# remembers the table, plus the column's name, id, and data type.
payload = []
for table in tables:
    response = requests.get(
        BASE_URL + "/api/fields",
        headers=HEADERS,
        params={"container_id": table["id"], "size": 100},
        verify=VERIFY_SSL,
    )
    response.raise_for_status()
    columns = response.json()["items"]

    print(
        "  Table: %s  (id %s)  ->  %s columns"
        % (table["name"], table["id"], len(columns))
    )
    for column in columns:
        print(
            "      - %-30s  id: %-8s  type: %s"
            % (column["name"], column["id"], column.get("type"))
        )
        payload.append(
            {
                "table_name": table["name"],
                "table_id": table["id"],
                "column_name": column["name"],
                "column_id": column["id"],
                "column_type": column.get("type"),
            }
        )

print()
print("  Extracted %s columns across %s table(s)." % (len(payload), len(tables)))


# =============================================================================
#  PART 2 - CREATE (POST): turn that payload into Not Null checks, in bulk
# =============================================================================

print()
print("PART 2 - Creating Not Null checks (up to %s) ..." % MAX_CHECKS)
print()

# --- 2a. (Optional) create the tag so every check gets labeled ---------------
#     POST /api/global-tags
#     If the tag already exists Qualytics answers with an error - that is fine,
#     it just means the label is already there, so we ignore it and move on.
if TAG_NAME:
    requests.post(
        BASE_URL + "/api/global-tags",
        headers=HEADERS,
        json={"type": "global", "name": TAG_NAME, "color": "#2196F3"},
        verify=VERIFY_SSL,
    )

# --- 2b. Create one Not Null check per column ---------------------------------
#     POST /api/quality-checks
#
# Three things can happen for each column, and we keep count of all three:
#   CREATED        - the check was created (the normal case)
#   ALREADY EXISTS - Qualytics answers "409 Conflict" because an equivalent
#                    check already covers that column (for example one that
#                    Qualytics inferred automatically). Nothing gets duplicated;
#                    that column was already protected. We note it and move on.
#   error          - anything else (bad token, deleted column, ...)
created = 0
already_existed = 0
errors = 0

for entry in payload:
    if created >= MAX_CHECKS:
        print()
        print("  Reached the safety limit of %s checks - stopping here." % MAX_CHECKS)
        break

    # This is the whole request body needed to create a check:
    check = {
        "container_id": entry["table_id"],  # which table
        "fields": [entry["column_name"]],  # which column
        "rule": "notNull",  # the rule type
        "description": "%s must never be empty (created in bulk via the Qualytics API)"
        % entry["column_name"],
    }
    if TAG_NAME:
        check["tags"] = [TAG_NAME]

    response = requests.post(
        BASE_URL + "/api/quality-checks", headers=HEADERS, json=check, verify=VERIFY_SSL
    )

    if response.ok:
        created += 1
        new_check = response.json()
        print(
            "  CREATED         check #%-6s %s . %s"
            % (new_check.get("id", "?"), entry["table_name"], entry["column_name"])
        )
    elif response.status_code == 409:
        # 409 Conflict = this column already has an equivalent check.
        # The API even tells us which one, e.g.
        #   "The existing check with id: 3381 conflicts"
        already_existed += 1
        detail = response.json().get("detail", "a check already exists")
        print(
            "  ALREADY EXISTS  %s . %s  (%s)"
            % (entry["table_name"], entry["column_name"], detail)
        )
    else:
        errors += 1
        try:
            detail = response.json().get("detail", "")
        except ValueError:
            detail = response.text[:120]
        print(
            "  error %s       %s . %s  (%s)"
            % (response.status_code, entry["table_name"], entry["column_name"], detail)
        )


# =============================================================================
#  Summary
# =============================================================================

print()
print("=" * 62)
print("Done!")
print("   New checks created ....... %s" % created)
if already_existed:
    print("   Already existed ......... %s  (those columns were already" % already_existed)
    print("                                 covered - nothing was duplicated)")
if errors:
    print("   Errors .................. %s  (see the messages above)" % errors)
print("=" * 62)
if TAG_NAME:
    print(
        "Tip: in the Qualytics app, filter checks by the tag '%s' to see them all."
        % TAG_NAME
    )
print()
