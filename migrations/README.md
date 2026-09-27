# ScoutChain — Database Migrations

This directory contains the PostgreSQL schema migrations for the ScoutChain
backend event indexer. Each migration is a numbered SQL file that is applied
in ascending order to bring the database schema up to date.

## Migration ownership

**SQL migrations are the canonical source of truth for the database schema.**

The project uses two schema representations:

| Representation | Location | Authority |
|----------------|----------|-----------|
| SQL migrations | `migrations/*.sql` | **Canonical** — applied by the backend on startup or by a DBA |
| Prisma schema | `prisma/schema.prisma` | **Derived** — must be kept in sync with the SQL migrations |

When the two representations diverge, the SQL migration wins. If you add or
change a table, write the SQL migration first, then update `prisma/schema.prisma`
to match. Never apply a `prisma migrate` command against a production database
without a corresponding SQL migration in this directory.

## Prisma mapping convention

Prisma model names use PascalCase; the corresponding SQL table names use
snake_case. Every Prisma model must declare a `@@map` annotation that names
the SQL table:

```prisma
model RevokedToken {
  jti       String   @id @db.VarChar(128)
  createdAt DateTime @default(now()) @map("created_at") @db.Timestamptz

  @@map("revoked_tokens")
}
```

This ensures that Prisma-generated queries target the correct table name
regardless of the Prisma model name.

## Naming and numbering convention

Files must be named `NNN_description.sql` where `NNN` is a zero-padded
three-digit integer incremented by one for each new migration:

```
001_initial_schema.sql
002_cursor_upsert_helper.sql
003_diagnostic_events.sql
004_revoked_tokens.sql
005_...
```

Never reuse or skip a number. Never rename an existing migration file after it
has been applied to any environment (local, testnet, or mainnet).

## Idempotency requirement

Every migration must be safe to re-run against an already-migrated database.
Use `IF NOT EXISTS` guards for `CREATE TABLE`, `CREATE INDEX`, `CREATE FUNCTION`,
and `CREATE TYPE`. Use `ON CONFLICT DO NOTHING` for seed `INSERT` statements.

Example:

```sql
CREATE TABLE IF NOT EXISTS my_table (
    id   SERIAL PRIMARY KEY,
    name TEXT   NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_my_table_name ON my_table (name);
```

## Applying migrations

Run each migration file in order against your PostgreSQL instance:

```bash
# Apply a single migration
psql $DATABASE_URL -f migrations/004_revoked_tokens.sql

# Apply all migrations in order (example using a shell loop)
for f in migrations/*.sql; do
    echo "Applying $f..."
    psql "$DATABASE_URL" -f "$f"
done
```

The backend service applies all migrations automatically on startup using the
ordering defined above. See `docs/DEPLOYMENT.md` for the full deployment guide.

## Current migrations

| File | Purpose |
|------|---------|
| `001_initial_schema.sql` | Fourteen core tables: players, scouts, validators, milestones, scout_subscriptions, contact_records, trial_offers, fee_withdrawals, admin_transfers, and the indexer_cursor checkpoint |
| `002_cursor_upsert_helper.sql` | `advance_indexer_cursor(bigint)` helper function for idiomatic cursor advancement without hand-written `ON CONFLICT` clauses |
| `003_diagnostic_events.sql` | `diagnostic_events` table for off-chain indexing of observability events (level advancement skipped, progress contract not wired, cross-contract call failures) |
| `004_revoked_tokens.sql` | `revoked_tokens` table for explicit JWT revocation on sign-out and credential rotation |
