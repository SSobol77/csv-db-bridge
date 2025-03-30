![15_36_23](https://github.com/user-attachments/assets/57718e79-5e8e-4201-bc49-168ab52ace60)

[![Build Status](https://github.com/SSobol77/csv-db-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/SSobol77/csv-db-bridge/actions)
[![Python Versions](https://img.shields.io/badge/python-3.11%20|%203.12%20|%203.13-blue.svg)](https://www.python.org/)

<br>

# **csv-db-sdk** 

> *csv-db-sdk** is a universal, cross-database toolkit written in Python to import and export data between `.csv` files and the most popular relational and non-relational databases.

Supported operations:
- 📥 Import from CSV/CLI to database
- 📤 Export from database to CSV

Supported databases:
- PostgreSQL
- MySQL
- SQLite3
- Oracle
- AuroraDB (AWS RDS Data API)
- IBM DB2
- MongoDB

---

## 🚀 Features

- Consistent import/export structure
- Modular scripts for each database
- Example scripts and unit tests
- CI/CD via GitHub Actions
- FreeBSD support via Cirrus CI

---

## 📁 Project Structure

```
csv-db-sdk/
├── import/                # CSV ➔ DB (write)
├── export/                # DB ➔ CSV (read)
├── examples/              # Usage examples
├── tests/                 # Unit tests with mocks
├── docs/                  # Architecture documentation
├── .github/workflows/     # GitHub Actions (CI)
├── .cirrus.yml            # FreeBSD CI with Cirrus
├── README.md              # You are here
└── LICENSE                # GPL-3.0 License
```

---

## 🛠 Requirements

- Python 3.11–3.13  
- pip packages:
  - `psycopg2-binary`, `mysql-connector-python`, `sqlite3`, `cx_Oracle`
  - `pymongo`, `boto3`, `ibm-db`

Install all:

```bash
pip install -r requirements.txt
```

---

## 💪 Run Tests

GitHub Actions will automatically test all files.  
To run tests locally:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

---

## 📄 License

Licensed under **GNU GPL v3.0**  
See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Siergej Sobolewski**  
📧 [s.sobolewski@hotmail.com](mailto:s.sobolewski@hotmail.com)  
🔗 GitHub: [SSobol77](https://github.com/SSobol77)

