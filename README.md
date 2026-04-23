# ophix-dbengine-postgres

PostgreSQL database engine plugin for [ophix-server-base](https://github.com/ophixproject/ophix-server-base).

Bundles `psycopg2-binary`. Set `DB_ENGINE=postgres` in `.env` to use it.

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
