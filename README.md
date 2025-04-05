![15_36_23](https://github.com/user-attachments/assets/57718e79-5e8e-4201-bc49-168ab52ace60)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Versions](https://img.shields.io/badge/python-3.11%20|%203.12%20|%203.13-blue.svg)](https://www.python.org/)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![FreeBSD](https://img.shields.io/badge/FreeBSD-AB2B28?logo=freebsd&logoColor=white)

<br>

<div align="center">
  <h1>📦 CSV-DB-SDK</h1>
  <h3>Universal Database Integration SDK for CSV Operations</h3>
</div>

<br>

---

<br>

> [!IMPORTANT]
> **🚫 Ethical Restrictions**
> 
> My works cannot be used in:
> 
> - Military applications or systems  
> - Surveillance technologies  
> - Any activity violating human rights  

<br>

---

## 🚀 **Features**

| **Category**       | **Details**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Core Operations** | 📥 CSV-to-DB Import • 📤 DB-to-CSV Export • 🔄 Bidirectional Sync           |
| **Database Support**| ✅ PostgreSQL • ✅ MySQL • ✅ SQLite • 🚀 MongoDB • ☁️ AWS Aurora • 🏢 Oracle • 🖥️ IBM DB2 |
| **SDK Advantages**  | 🧩 Modular Design • 📚 Client Libraries • 🛠 CLI Tools • 🧪 Mock Testing Framework |

---

## ⚡ **Quick Start**

### **Installation**
```bash

# Clone repository
git clone https://github.com/SSobol77/csv-db-sdk.git
cd csv-db-sdk

# Basic Installation (Core Functionality)
pip install csv-db-sdk

# Development Setup (Testing + Coverage)
pip install "csv-db-sdk[testing]"

# Full Installation (All Features)
pip install "csv-db-sdk[full]"
```
<br>

### Semantic Versioning Policy

##### Dependency Management
Strict SemVer compliance for all dependencies:
psycopg2-binary ~= 2.9.9    # Compatible with 2.9.x (2.9.9 ≤ version < 3.0)
boto3 ~= 1.34.112           # Compatible with 1.34.x (1.34.112 ≤ version < 2.0)

##### Version Guarantees
- Major versions (X.0.0): Breaking API changes
- Minor versions (1.X.0): Backwards-compatible features
- Patch versions (1.0.X): Backwards-compatible bug fixes

<br>

### Compatibility Matrix
| Component       | Supported Versions | Stability Level |
|-----------------|--------------------|-----------------|
| PostgreSQL      | 12-16              | Production      |
| MySQL           | 5.7-8.1            | Production      |
| Oracle DB       | 19c-23c            | Verified        |
| MongoDB         | 4.4-7.0            | Production      |

<br>

### Upgrade Recommendations

```bash
# Safe Upgrade Path
pip install --upgrade-strategy eager "csv-db-sdk>=1.2,<2.0"

# Version Pinning Example
echo "csv-db-sdk==1.2.3" >> production-requirements.txt
```
<br>

### **Basic Usage**
```python
from csv_db_sdk import PostgresConnector

# Initialize connector
config = {
    "host": "localhost",
    "user": "admin",
    "password": "secret",
    "database": "mydb"
}
pg = PostgresConnector(config)

# Import CSV to table
pg.import_csv("data/users.csv", "users_table")

# Export table to CSV
pg.export_csv("analytics/results.csv", "sales_data")

```

---

<br>

## 🏗 **Architecture**

```bash
csv-db-sdk/
├── 📂 core/               # SDK Core Components
│   ├── connectors.py      # Base DB connector logic
│   └── utilities.py       # CSV parsing/validation
├── 📂 db_adapters/        # Database-specific implementations
│   ├── postgres.py        # PostgreSQL adapter
│   ├── mongodb.py         # MongoDB adapter
│   └── ...                # Other databases
├── 📂 examples/           # Ready-to-run scenarios
│   ├── basic_import.py    # CSV → DB example
│   └── advanced_export.py # DB → CSV with filtering
└── 📂 tests/              # Comprehensive test suite
    ├── unit/              # Isolated component tests
    └── integration/      # End-to-end workflow tests
```

---

<br>

## 🔧 **Database Configuration**

### **Connection Templates**
```yaml
# PostgreSQL Example
postgres:
  host: "db-server.prod"
  port: 5432
  database: "analytics"
  user: "${DB_USER}"
  password: "${DB_PASS}"
  sslmode: "require"

# MongoDB Example
mongodb:
  uri: "mongodb+srv://cluster.prod.mongodb.net"
  authSource: "admin"
  tls: true
```

---

## 🧪 **Testing Strategy**

**Multi-level Validation:**
```bash
# Run all tests
pytest tests/ -v

# Test specific database
pytest tests/postgres -v --cov=db_adapters.postgres

# Generate coverage report
pytest --cov-report html --cov=.
```

| **Test Type**     | **Coverage**                          | **Tools Used**            |
|--------------------|---------------------------------------|---------------------------|
| Unit Testing       | 92% Core logic                       | pytest, unittest          |
| Integration Tests  | 85% DB-specific workflows            | Docker, Testcontainers    |
| Performance Bench  | 10k rows/sec (PostgreSQL)            | Locust, pyperf            |

---

## 🤝 **Contributing**

1. Fork the repository
2. Create feature branch: `git checkout -b feat/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feat/amazing-feature`
5. Open Pull Request

---

## 📜 **License**

**GNU GPLv3** - See [LICENSE](LICENSE) for full text.  
📌 Commercial use requires special permission - contact author for details.

---

## 📬 **Contact**

**Siergej Sobolewski**  
[![Email 🚀](https://img.shields.io/badge/Email-s.sobolewski@hotmail.com-blue?logo=protonmail)](mailto:s.sobolewski@hotmail.com)  
[![GitHub](https://img.shields.io/badge/GitHub-SSobol77-blue?logo=github)](https://github.com/SSobol77)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/siergej-s-25a16319a)

