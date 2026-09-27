# ScoutChain — Configuration Reference

All environment variables consumed anywhere in this repository are listed below,
grouped by component. Copy `.env.example` to `.env` and fill in every **Required**
value before running scripts or starting the backend.

---

## Stellar / Soroban — Deployment & Contract Invocation

These variables are read by the deployment and initialization shell scripts:
`scripts/deploy.sh`, `scripts/initialize.sh`, `scripts/generate-bindings.sh`,
`scripts/setup-testnet.sh`, and `testnet/seed.sh`.

| Variable | Consumer | Required / Optional | Notes |
|---|---|---|---|
| `DEPLOYER_SECRET` | `scripts/deploy.sh`, `scripts/initialize.sh`, `testnet/seed.sh` | **Required** | Stellar secret key (`S...`) used to sign deployment and invocation transactions |
| `ADMIN_ADDRESS` | `scripts/initialize.sh`, `testnet/seed.sh` | **Required** | Stellar G-address set as admin on all four contracts. Cannot be changed after `initialize`. |
| `XLM_TOKEN_ADDRESS` | `scripts/initialize.sh` | **Required** | Native XLM token contract address. Testnet: `CDLZFC3SYJYDZT7K67VZ75HPJVIEUVNIXF47ZG2FB2RMQQVU2HHGCYSC`. Mainnet: `CAS3J7GYLGXMF6TDJBBYYSE3HQ6BBSMLNUQ34T6TZMYMW2EVH34XOWMA` |
| `STELLAR_NETWORK` | `scripts/deploy.sh`, `scripts/initialize.sh`, `scripts/generate-bindings.sh` | Optional | `testnet` or `mainnet`. Defaults to `testnet`. |
| `HORIZON_URL` | `testnet/seed.sh` | Optional | Horizon REST API endpoint. Default: `https://horizon-testnet.stellar.org` |
| `SOROBAN_RPC_URL` | `scripts/deploy.sh`, `scripts/initialize.sh` | Optional | Soroban JSON-RPC endpoint. Default: `https://soroban-testnet.stellar.org` |

---

## Contract IDs

Written to `.env.contracts` by `scripts/deploy.sh`. Must be copied into the backend
and frontend repos after deployment. Also consumed directly by
`scripts/initialize.sh`, `scripts/generate-bindings.sh`, `testnet/seed.sh`, and
`scripts/reconcile-indexer.js`.

| Variable | Consumer | Required / Optional | Notes |
|---|---|---|---|
| `REGISTRATION_CONTRACT_ID` | `scripts/initialize.sh`, `scripts/generate-bindings.sh`, `testnet/seed.sh`, `scripts/reconcile-indexer.js` | **Required** (post-deploy) | Contract ID of the deployed `registration` contract |
| `VERIFICATION_CONTRACT_ID` | `scripts/initialize.sh`, `scripts/generate-bindings.sh`, `testnet/seed.sh` | **Required** (post-deploy) | Contract ID of the deployed `verification` contract |
| `PROGRESS_CONTRACT_ID` | `scripts/initialize.sh`, `scripts/generate-bindings.sh`, `testnet/seed.sh` | **Required** (post-deploy) | Contract ID of the deployed `progress` contract |
| `SCOUT_ACCESS_CONTRACT_ID` | `scripts/initialize.sh`, `scripts/generate-bindings.sh`, `testnet/seed.sh`, `scripts/reconcile-indexer.js` | **Required** (post-deploy) | Contract ID of the deployed `scout_access` contract |

---

## WASM Hashes

Written to `.env.contracts` by `scripts/deploy.sh`. Used to verify the on-chain WASM
binary identity matches the locally built artifact.

| Variable | Consumer | Required / Optional | Notes |
|---|---|---|---|
| `REGISTRATION_CONTRACT_WASM_HASH` | `scripts/deploy.sh` (output) | Optional | SHA-256 hash of the deployed registration WASM |
| `VERIFICATION_CONTRACT_WASM_HASH` | `scripts/deploy.sh` (output) | Optional | SHA-256 hash of the deployed verification WASM |
| `PROGRESS_CONTRACT_WASM_HASH` | `scripts/deploy.sh` (output) | Optional | SHA-256 hash of the deployed progress WASM |
| `SCOUT_ACCESS_CONTRACT_WASM_HASH` | `scripts/deploy.sh` (output) | Optional | SHA-256 hash of the deployed scout_access WASM |

---

## Backend / Node.js

Read by the TypeScript application server and the Node.js reconciler script.

| Variable | Consumer | Required / Optional | Notes |
|---|---|---|---|
| `DATABASE_URL` | `prisma/schema.prisma`, `scripts/reconcile-indexer.js` | **Required** | PostgreSQL connection string used by Prisma ORM and the indexer reconciler. Format: `postgresql://USER:PASSWORD@HOST:PORT/DATABASE` |
| `JWT_SECRET` | `src/middleware/auth.ts` | **Required** | Secret used to sign and verify JWT bearer tokens. Use a cryptographically random value (`openssl rand -hex 32`). Never commit the real value. |

---

## Notes

- Never commit a populated `.env` file. It is listed in `.gitignore`.
- After running `scripts/deploy.sh`, copy `.env.contracts` values into your backend
  and frontend `.env` files — they are not automatically forwarded.
- For mainnet deployments, verify `config/mainnet.json` has no placeholder values
  (`FILL_IN_BEFORE_USE`) before running `scripts/deploy.sh mainnet`.
