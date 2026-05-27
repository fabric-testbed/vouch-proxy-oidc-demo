# SSL - certificates for development

Since [CILogon](https://www.cilogon.org) requires a secure connection as an OIDC Relying Party, a TLS certificate and private key are required for local development.

The following files are expected at the root of this `ssl/` directory and are mounted into the Nginx container at `/etc/ssl/` (see `nginx/default.conf`):

- `privkey.pem`  : the private key for your certificate.
- `fullchain.pem`: the certificate file used in most server software (copy of `chain.pem` for development purposes).
- `chain.pem`    : used for OCSP stapling in Nginx >=1.3.7.

> **Important:** these files are **not** checked into the repository. Private keys must never be committed to source control. The previously committed development certificates were removed after GitHub secret scanning flagged the private key; if you cloned the repo before that change, delete any local copies and regenerate them with the steps below. The files are also listed in the top-level `.gitignore` to prevent accidental re-commit.

The certificates generated below are self-signed and not recognized by any CA. Do not use them for anything beyond local development (never use in production).

## Generate `privkey.pem`, `fullchain.pem`, and `chain.pem`

Certificate generation is based on Let's Encrypt's guidance for [certificates for localhost](https://letsencrypt.org/docs/certificates-for-localhost/).

From the repository root, run:

```bash
cd ssl

openssl req -x509 -outform pem -out chain.pem -keyout privkey.pem \
  -newkey rsa:4096 -nodes -sha256 -days 3650 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

cat chain.pem > fullchain.pem
```

This produces three files in `ssl/`:

| File            | Purpose                                                                 |
| --------------- | ----------------------------------------------------------------------- |
| `privkey.pem`   | RSA 4096-bit private key (kept local, never commit).                    |
| `chain.pem`     | Self-signed X.509 certificate valid for `localhost` for 3650 days.      |
| `fullchain.pem` | Copy of `chain.pem` used as `ssl_certificate` by Nginx.                 |

After generating, restart the stack (e.g. `docker compose restart nginx`) so Nginx picks up the new files.

## Trusting the certificate locally (optional)

Because the certificate is self-signed, browsers will display a warning the first time you visit `https://localhost`. To suppress the warning during development, import `chain.pem` into your operating system or browser trust store as a trusted root.

## Reference

Nginx configuration reference: [https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/)
