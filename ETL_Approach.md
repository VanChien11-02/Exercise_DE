# ETL Pipeline Approach

## Overview
This project builds a simple ETL pipeline for customer transaction data. The pipeline reads data from three CSV files: `customers.csv`, `transactions.csv`, and `products.csv`, cleans the data, and loads the processed data into SQL Server.

## Extract
The CSV files are loaded into Python using `pandas`.

## Transform
The data is cleaned before loading:
- Invalid or missing customer emails are handled.
- Invalid transaction dates are converted to `NaT`. Despite date is invalid but amount is still valid so it don't need remove
- Duplicate transactions are removed using `transaction_id`.
- Product categories are standardized to a consistent format.

## Load
The cleaned data is loaded into three SQL Server tables:
- `customers`
- `products`
- `transactions`

The parent tables `customers` is loaded before `transactions` to avoid foreign key errors.

## Data Aggregation
A SQL query is used to calculate the total transaction amount for each customer. The result is stored in a new table called `customer_revenue`.

## Validation
After the pipeline runs, the loaded tables are checked in SQL Server to make sure the cleaned data was inserted correctly and invalid records were removed.
