#!/usr/bin/env python3
# Qualytics API readiness check - four read-only calls, top to bottom.
#
# STEP 1: Fill in your two values right here between the quotes:
BASE = "https://your-instance.qualytics.io"  # <-- your Qualytics web address
TOKEN = "my-qualytics-api-token"  # <-- your API token (like a keycard)

# STEP 2: Save this file, then run it:
#   python3 check_api.py

import json
import ssl
import urllib.request

# HTTPS setup. Some Python installs (very common on Mac) come without the
# list of trusted certificates and fail with "CERTIFICATE_VERIFY_FAILED".
# If the "certifi" package is installed, we use its certificate list.
# (Fix for that error: run once in the terminal ->  pip3 install certifi )
try:
    import certifi

    context = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    context = ssl.create_default_context()
urllib.request.install_opener(
    urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
)

BASE = BASE.rstrip("/")
AUTH = {"Authorization": "Bearer " + TOKEN}

print("Checking " + BASE)
print()

# 1) Is the platform on?  (public - no token needed; healthy = code 204)
r = urllib.request.urlopen(BASE + "/api/health", timeout=15)
print(
    "1) Platform on?           ",
    "PASS" if r.status == 204 else "FAIL (code %s)" % r.status,
)

# 2) Is it healthy inside?  (public - reports database + internal messaging)
r = urllib.request.urlopen(BASE + "/api/status", timeout=15)
body = json.load(r)
ok = body.get("database_connection") == "OK" and body.get("rabbitmq_connection") == "OK"
print("2) Internals healthy?     ", "PASS" if ok else "FAIL " + str(body))

# 3) Does the token work?  (asks the API: "who am I?")
req = urllib.request.Request(BASE + "/api/users/me", headers=AUTH)
r = urllib.request.urlopen(req, timeout=15)
body = json.load(r)
print(
    "3) Token works?            PASS - you are %s (role: %s)"
    % (body.get("name"), body.get("role"))
)

# 4) Can we read data?  (ask for exactly one past operation)
req = urllib.request.Request(BASE + "/api/operations?size=1", headers=AUTH)
r = urllib.request.urlopen(req, timeout=15)
body = json.load(r)
print("4) Can read data?          PASS - %s operations visible" % body.get("total"))

print()
print("API is ready.")

# If anything above fails, Python stops right there and prints the error:
#   - "HTTP Error 401" on step 3 or 4      = token is wrong or expired
#   - "URLError" / timeout                 = wrong URL, no internet, or VPN needed
#   - "CERTIFICATE_VERIFY_FAILED"          = your Python is missing its certificate
#     list (common on Mac). Fix it once with:   pip3 install certifi
#     (or double-click "Install Certificates.command" in your Python folder)
