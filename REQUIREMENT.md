Exercise for Level 2 Data Engineer (Middle)

Scenario: Customer Transaction Pipeline
You are a Data Engineer tasked with creating an ETL pipeline to process customer transaction data for a retail company. The company’s data comes from multiple sources and must be cleaned, transformed, and loaded into a relational database for analysis.
Input files: 
   - customers.csv
   - transactions.csv
   - products.csv

### Task Description:
#### 1.	Data Cleaning and Transformation:
    - You are provided with three CSV files:
    1.	customers.csv: Contains customer information, but some rows have invalid or missing email addresses.
    2.	transactions.csv: Contains transaction data but includes invalid transaction dates (e.g., 2024-13-45) and duplicate entries.
    3.	products.csv: Contains product details, but some rows have inconsistent product categories (e.g., "Electronics" and "electronics").
    - Your task is to:
        - Clean the data to handle missing and invalid values.
        - Standardize product categories and ensure valid email formats.
        - Deduplicate the transaction data.
#### 2.	ETL Pipeline:
    - Build a Python script to implement the ETL pipeline:
        - Extract the data from the CSV files.
        - Transform the data according to the cleaning rules above.
        - Load the cleaned data into a SQLite database with three tables: customers, transactions, and products.
#### 3.	Data Aggregation:
    - Write a SQL query to calculate the total transaction amount per customer and save the results in a new table called customer_revenue.
#### 4.	Deliverables:
    - The Python script for the ETL pipeline.
    - The cleaned data in the SQLite database.
    - The SQL query for customer revenue aggregation.

You must submit:
•	Your code in the form of a GitHub repository or ZIP file.
•	Screenshots or log outputs showing the results of your pipeline runs.
•	A brief document explaining your approach.

