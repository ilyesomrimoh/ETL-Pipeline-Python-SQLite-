# Mini ETL Pipeline – COVID-19 Data

## Overview

This is a small ETL (Extract, Transform, Load) project that takes COVID-19 data from a CSV file, cleans it, and stores it in a database. It demonstrates how raw data can be prepared and organized for analysis.

## Steps

1. **Extract**
   Reads the CSV file (`covid_19_data.csv`) containing daily COVID-19 cases by country and province.

2. **Transform**

   * Fills empty province names with “Unknown”
   * Converts dates to the correct format
   * Removes rows with missing critical data
   * Recalculates active cases to ensure consistency
   * Keeps only the important columns for analysis

3. **Load**
   Saves the cleaned data into a SQLite database (`covid19.db`).
   It also runs simple queries to check the number of rows and find the top 5 countries by confirmed cases.

## How to Run

1. Make sure you have Python 3 installed.
2. Install required packages:

   ```
   pip install pandas
   ```
3. Organize files like this:

   ```
   mini_etl_project/
   ├─ data/
   │   └─ covid_19_clean_complete.csv
   ├─ scripts/
   │   ├─ extract.py
   │   ├─ transform.py
   │   └─ load.py
   └─ main.py
   ```
4. Run the pipeline:

   ```
   python main.py
   ```

## Outcome

After running, you will have:

* A **cleaned COVID-19 dataset** stored in a database
* A small, functional **ETL pipeline** ready for analysis
* Validation queries to check data consistency

## Skills Demonstrated

* Python programming
* Data cleaning and transformation
* SQLite database handling
* Modular, reusable code for ETL pipelines
