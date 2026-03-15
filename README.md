# CSV Data Utility

A professional **CLI tool** to clean CSV files automatically.  
It helps prepare messy CSV data by:

- Stripping unnecessary whitespace
- Removing rows with null values
- Validating date formats
- Separating invalid rows into a discarded file

This tool is useful for **data preprocessing before analysis or machine learning pipelines**.

---

# Installation & Setup

Clone the repository and go to the project folder:

```bash
git clone https://github.com/SamratGhimire01/cli-data-utility.git
cd cli-data-utility
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the CLI command:

```bash
pip install -e .
```

---

# Usage

Run the CLI command:

```bash
csv-clean --input data/data.csv --output data/Updated_file.csv --dfile data/discarded_data.csv
```

---

# Command Arguments

| Argument | Description |
|--------|-------------|
| `--input` | Path to the source CSV file (Required) |
| `--output` | Path where cleaned data will be saved |
| `--dfile` | Path where invalid rows will be stored |

---

# Example

```bash
csv-clean \
--input data/data.csv \
--output data/clean_data.csv \
--dfile data/discarded_rows.csv
```

---

# Author

Samrat Ghimire