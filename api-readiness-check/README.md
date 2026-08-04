# Qualytics API readiness check

Answers one question: **"Is the Qualytics API up, and can my token use it?"**

| File | What it is |
|---|---|
| `check_api.py` | A short Python script — runs all four checks and prints PASS/FAIL |
| `curl-examples.md` | The same four calls as copy-paste curl commands, one by one |

Nothing here changes any data — every call only **reads**.

## The four checks, in plain words

Like calling a restaurant before driving there:

1. **Does anyone pick up?** — is the platform on? (`/api/health`, no token needed)
2. **Is the kitchen open?** — database and internal messaging healthy? (`/api/status`, no token needed)
3. **Do they have my reservation?** — does my token work? (`/api/users/me`)
4. **Can I see the menu?** — can I actually read data? (`/api/operations?size=1`)

## How to run

1. Open `check_api.py` in any text editor.
2. At the top, fill in your two values between the quotes:
   your Qualytics web address and your API token.
3. Save the file, then in a terminal run:

```bash
python3 check_api.py
```

The token is like a keycard — never share it or paste it into documents.
For the curl versions, open `curl-examples.md` — it starts with two `export`
lines to set your address and token, then every command copy-pastes as-is.

## If something fails

- **Steps 1–2** → platform or URL problem (wrong address, VPN, platform down). Not your token's fault.
- **Steps 3–4** → token problem (expired, mis-copied) or missing permission.
