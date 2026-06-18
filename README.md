# Mini Test Platform

A lightweight test automation platform built with Python.

## Features

- Load test cases from JSON files
- Execute automated test cases
- Generate HTML test reports
- YAML-based configuration
- Logging support
- Test statistics summary
- Exception handling
- Execution time collection

---

## Architecture

```text
Loader
  ↓
Runner
  ↓
Statistics
  ↓
Reporter
```

### Components

#### Loader

Responsible for loading test cases from JSON files.

#### Runner

Responsible for executing test cases and collecting results.

#### Statistics

Calculates:

- Total
- Passed
- Failed
- Pass Rate
- Execution Time

#### Reporter

Generates HTML reports.

---

## Project Structure

```text
mini_test_platform/

├── config/
│   └── config_loader.py
│
├── loader/
│   └── test_loader.py
│
├── runner/
│   └── test_runner.py
│
├── reporter/
│   └── html_reporter.py
│
├── utils/
│   └── statistics.py
│
├── tests/
│   └── test_cases.json
│
├── logs/
│
├── reports/
│
├── config.yaml
│
├── main.py
│
└── README.md
```

---

## Configuration

Example:

```yaml
test_case_path: tests/test_cases.json

report:
  output_dir: reports
  report_name: report.html

log:
  level: INFO
  log_file: logs/test.log
```

---

## Test Case Format

Example:

```json
[
  {
    "name": "test_add",
    "input": [1, 2],
    "expected": 3
  },
  {
    "name": "test_add_fail",
    "input": [2, 2],
    "expected": 5
  }
]
```

---

## Run

Execute:

```bash
python main.py
```

Or specify configuration file:

```bash
python main.py config_prod.yaml
```

---

## Sample Report

```text
-------------------------------------
 Test Report
-------------------------------------

Total: 2
Passed: 1
Failed: 1

-------------------------------------
| Case Name     | Status | Duration |
-------------------------------------
| test_add      | PASS   | 0.01 ms  |
| test_add_fail | FAIL   | 0.02 ms  |
-------------------------------------
```

---

## Future Enhancements

- Multiple reporters (HTML / CSV)
- Pytest integration
- CI/CD integration
- Database result storage
- Web dashboard

---

## Technology Stack

- Python
- JSON
- YAML
- Logging
- HTML

---
