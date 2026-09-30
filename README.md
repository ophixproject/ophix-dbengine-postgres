# ophix-dbengine-postgres

**Already running Postgres everywhere else? Your [Ophix](https://ophix.io) server can too.**

Standing up one more database engine just for a fleet-management tool is exactly the kind of avoidable infrastructure sprawl nobody wants. `ophix-dbengine-postgres` lets any Ophix server (creds, tasks, confs, certs, zones) run against the Postgres instance you already operate — install the plugin, set `DB_ENGINE=postgres`, done.

Bundles `psycopg2-binary`.

---

## Installation

```bash
pip install ophix-dbengine-postgres
```

Set in `.env`:

```bash
DB_ENGINE=postgres
DB_HOST=your-postgres-host
DB_PORT=5432
DB_NAME=ophix_db
DB_USER=ophixuser
DB_PASSWORD=yourpassword
```

For TLS, set `DB_SSL_CA` to the path of your CA certificate.
