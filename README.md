
---

### 🔷 Scalable JSON Hive ETL using PySpark

This project demonstrates a simple and scalable **ETL (Extract, Transform, Load)** pipeline built with **Apache Spark 4.0.0** using **PySpark**. It reads **JSON files**, processes the data using Spark DataFrames, and writes the output into **Parquet** format, suitable for further analysis or loading into **Apache Hive**.

---

### 📌 Features

* 🔹 Reads JSON data using PySpark
* 🔹 Parses and displays structured data
* 🔹 Writes output in optimized **Parquet** format
* 🔹 Prepares data for Hive ingestion
* 🔹 Built with **Spark 4.0.0**, compatible with Hadoop ecosystem

---

### 📂 Folder Structure

```
scalable-json-hive-etl/
│
├── data/                      # Input JSON data
│   └── sample.json
│
├── etl/                       # ETL Python scripts
│   └── spark_etl.py
│
├── warehouse/                # Output Parquet files (auto-created)
│
├── README.md                 # Project description
└── requirements.txt          # Python dependencies
```

---

### 🚀 Run Locally

1. Set up virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install pyspark
   ```

2. Run the ETL script:

   ```bash
   python etl/spark_etl.py
   ```

3. Output will be stored in `warehouse/output_parquet/`.

---

### 📄 Sample Input (`data/sample.json`)

```json
[
  {"id": 1, "city": "Bangalore"},
  {"id": 2, "city": "Hyderabad"}
]
```

