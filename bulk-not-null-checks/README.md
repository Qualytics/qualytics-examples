# Bulk "Not Null" Check Creation via the Qualytics API

This example shows how to use the Qualytics REST API to create data quality
checks **in bulk**: it reads the tables and columns of a datastore, then
creates one simple **Not Null** check per column (up to a configurable limit).

A *Not Null* check is the simplest quality rule there is — it flags any row
where the column is empty. That makes it perfect for demonstrating scale:
one short script, ~50 checks created in seconds.

## Files

| File | What it is |
|------|------------|
| `bulk_not_null_checks.py` | The demo script. Heavily commented, no parameters — you edit 4 values at the top and run it. |
| `README.md` | This document. |

## How to run it

1. Install the one dependency (most machines already have it):

   ```bash
   pip3 install requests
   ```

2. Open `bulk_not_null_checks.py` and fill in the settings block at the top:

   | Setting | What to put there |
   |---------|-------------------|
   | `BASE_URL` | Your Qualytics instance address, e.g. `https://acme.qualytics.io` |
   | `API_TOKEN` | A personal API token (see below) |
   | `DATASTORE_ID` | The datastore to work in — it's the number in the browser URL when you open the datastore in the app |
   | `TABLE_NAMES` | A list of table names, e.g. `["CUSTOMERS", "ORDERS"]`, or `[]` for **all** tables in the datastore |
   | `TAG_NAME` | Optional label applied to every created check (default `"API Demo"`) — makes the checks easy to find and clean up |
   | `MAX_CHECKS` | Safety limit; the script stops after creating this many checks (default 50) |

3. Run it:

   ```bash
   python3 bulk_not_null_checks.py
   ```

### Getting an API token

In the Qualytics app go to **Settings → Security → API Keys** and generate a
token. Every API request sends it in a header:

```
Authorization: Bearer <your token>
```

## The API endpoints the script uses

The script makes exactly four kinds of calls, in this order.

### 1. `GET /api/containers` — list the tables of a datastore

In the Qualytics API, tables (and views and files) are called **containers**.

```
GET {BASE_URL}/api/containers?datastore={DATASTORE_ID}&size=100
```

- `datastore` filters to one datastore.
- `size` is the page size (results are paginated; the response has an
  `items` list plus `total` / `page` bookkeeping).

Each item in `items` gives us the table's `id` and `name`.

### 2. `GET /api/fields` — list the columns of a table

Columns are called **fields**.

```
GET {BASE_URL}/api/fields?container_id={TABLE_ID}&size=100
```

Each item gives us the column's `name`, `id`, and declared data `type`
(e.g. `Integral`, `Fractional`, `String`, `Timestamp`). The script gathers
these into one payload — table name/id + column name/id/type — and prints it,
which is the "extract" half of the demo.

### 3. `POST /api/global-tags` — create the demo tag (optional)

```
POST {BASE_URL}/api/global-tags
```

```json
{ "type": "global", "name": "API Demo", "color": "#2196F3" }
```

If the tag already exists the API answers with an error; the script ignores
it on purpose (the label is already there, which is all we need).

### 4. `POST /api/quality-checks` — create one check (called in a loop)

This is the heart of the demo. One small JSON body per check:

```
POST {BASE_URL}/api/quality-checks
```

```json
{
  "container_id": 4211,
  "fields": ["CUSTOMER_ID"],
  "rule": "notNull",
  "description": "CUSTOMER_ID must never be empty (created in bulk via the Qualytics API)",
  "tags": ["API Demo"]
}
```

| Body field | Meaning |
|------------|---------|
| `container_id` | The table the check belongs to (from step 1) |
| `fields` | The column(s) the rule applies to (from step 2) |
| `rule` | The rule type — `notNull` here; the API supports many others (`unique`, `between`, `matchesPattern`, …) |
| `description` | Required free-text description shown in the app |
| `tags` | Optional list of tag names to label the check with |

A successful response returns the new check, including its `id`.

**About conflict errors (409):** if an equivalent check already exists on a
column (for example, one inferred automatically during profiling), the API
answers with **HTTP 409 Conflict** and a message naming the existing check:

```json
{ "detail": "The existing check with id: 3381 conflicts" }
```

That's expected and harmless — it means the column was already covered and
nothing gets duplicated. The script prints it as `ALREADY EXISTS` with the
API's message, keeps going, and reports the total in the final summary.

## What it looks like when it runs

```
PART 1 - Reading tables and columns from datastore 55 ...

  Table: CUSTOMERS  (id 4211)  ->  12 columns
      - CUSTOMER_ID                 id: 90101    type: Integral
      - FIRST_NAME                  id: 90102    type: String
      ...

  Extracted 57 columns across 4 table(s).

PART 2 - Creating Not Null checks (up to 50) ...

  CREATED         check #33810  CUSTOMERS . CUSTOMER_ID
  CREATED         check #33811  CUSTOMERS . FIRST_NAME
  ALREADY EXISTS  CUSTOMERS . EMAIL  (The existing check with id: 31204 conflicts)
  ...

==============================================================
Done!
   New checks created ....... 48
   Already existed ......... 9  (those columns were already
                                 covered - nothing was duplicated)
==============================================================
Tip: in the Qualytics app, filter checks by the tag 'API Demo' to see them all.
```

## Cleaning up after the demo

In the Qualytics app, go to the datastore's **Checks** tab, filter by the
tag `API Demo`, select all, and archive/delete them in one action.
