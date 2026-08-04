# Qualytics API — curl examples

The same four readiness checks as `check_api.py`, as copy-paste curl commands.
All of them only **read** — nothing changes any data.

Before running the commands, paste these two lines into your terminal
(with your own address and token between the quotes). "export" just means
"remember this value for the commands that follow":

```bash
export QUALYTICS_URL="https://your-instance.qualytics.io"
export QUALYTICS_TOKEN="paste-your-token-here"
```

After that, every command below can be copy-pasted exactly as written —
the `$QUALYTICS_URL` and `$QUALYTICS_TOKEN` parts fill themselves in.
The token is like a keycard — keep it private.

---

## 1) Is the platform on?

No token needed — this door is public on purpose.
A healthy platform answers with code `204`.

```bash
curl -i "$QUALYTICS_URL/api/health"
```

Expected first line: `HTTP/2 204`

---

## 2) Is it healthy inside?

Also public. Reports the two things the platform depends on —
its database and its internal messaging. Both should say `"OK"`.

```bash
curl "$QUALYTICS_URL/api/status"
```

Expected answer:

```json
{"database_connection": "OK", "rabbitmq_connection": "OK"}
```

---

## 3) Does your token work?

Asks the API "who am I?". The `-H "Authorization: ..."` part is the keycard swipe —
it sends your token along with the request.

```bash
curl -H "Authorization: Bearer $QUALYTICS_TOKEN" "$QUALYTICS_URL/api/users/me"
```

Expected: a JSON answer with your `name` and `role`.
If you get `401` instead, the token is wrong or expired.

---

## 4) Can you read data?

Asks for exactly **one** item from the operations history (`?size=1` = "just one, please").
This is the same endpoint the harvest scripts use, so if this works, everything works.

```bash
curl -H "Authorization: Bearer $QUALYTICS_TOKEN" "$QUALYTICS_URL/api/operations?size=1"
```

Expected: a JSON answer with a `total` count and one operation in `items`.

---

## Reading failures

| What you see | What it means |
|---|---|
| Steps 1–2 fail or time out | Platform or URL problem (wrong address, VPN, platform down) |
| Step 3–4 answer `401` | Token is wrong, expired, or copied incompletely |
| Step 3–4 answer `403` | Token works but lacks permission for that data |
