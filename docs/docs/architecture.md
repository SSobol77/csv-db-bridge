# Project Architecture – csv-db-bridge

## 🧩 Purpose

**csv-db-bridge** is a modular Python toolkit for importing and exporting data between CSV files and multiple database systems, both SQL and NoSQL.

Supported databases:
- PostgreSQL
- MySQL
- SQLite3
- Oracle
- AuroraDB
- IBM DB2
- MongoDB

It provides language-agnostic, consistent, and testable interfaces for each direction:
- `import/` — Import data from CSV or CLI into database
- `export/` — Export data from database into CSV

---

## 📁 Project Structure

```
csv-db-bridge/
├── import/             # CLI/CSV ➜ DB connectors
├── export/             # DB ➜ CSV extractors
├── examples/           # Usage samples
├── tests/              # Unit test per connector
├── docs/               # Project documentation
├── .github/workflows/  # CI/CD via GitHub Actions
├── README.md           # Main documentation
└── LICENSE             # GPL-3.0 License
```

---

## 🔄 Module Responsibilities

| Directory   | Purpose                              | Example Script             |
|-------------|--------------------------------------|----------------------------|
| `import/`   | Push `.csv` or console data into DB  | `imp_postgresql.py`        |
| `export/`   | Dump table data into `.csv` file     | `exp_sqlite3.py`           |
| `examples/` | Reproducible usage examples          | `example_postgresql.py`    |
| `tests/`    | Unit tests for logic + CLI calls     | `test_export_sqlite3.py`   |

---

## 🔧 Technical Stack

- **Language**: Python 3.11+
- **Databases**: SQL + NoSQL
- **Libraries**:
  - `psycopg2`, `mysql-connector-python`, `sqlite3`, `cx_Oracle`, `ibm_db`, `boto3`, `pymongo`
  - `csv`, `argparse`, `unittest`, `pytest`

---

##  Example Flow (Export PostgreSQL)

```text
1. Connect to PostgreSQL via psycopg2
2. Run SELECT * query on target table
3. Write result to CSV using Python's csv.writer
```

---

## 🔐 Security & Credentials

- Connection credentials should **never** be hardcoded in public deployments.
- Recommended practice: use `.env` file + `dotenv` or GitHub Actions secrets.

---

## 🛠 Future Extensions

- CLI entry point (`cli.py`) to handle all DBs from one interface
- Docker support
- Stream-based CSV handling (for large tables)
- Web GUI (Streamlit or Flask)

---

## 👤 Author

**Siergej Sobolewski**  
📧 s.sobolewski@hotmail.com  
🔗 https://github.com/SSobol77/csv-db-bridge

Licensed under GPL-3.0
