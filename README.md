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
<img width="1228" height="407" alt="image" src="https://github.com/user-attachments/assets/3a9d1f93-bc2a-491d-a6bf-06a06b9fa595" />


- `products`
<img width="673" height="379" alt="image" src="https://github.com/user-attachments/assets/a933d4cd-4359-4d5b-96fc-963967995036" />


- `transactions`
<img width="915" height="376" alt="image" src="https://github.com/user-attachments/assets/7bcfea2f-4a2d-481a-ba11-82a6c99d864c" />


The parent tables `customers` is loaded before `transactions` to avoid foreign key errors.

## Data Aggregation
A SQL query is used to calculate the total transaction amount for each customer. The result is stored in a new table called `customer_revenue`.
<img width="612" height="530" alt="image" src="https://github.com/user-attachments/assets/8325f6cd-96e1-4c2c-89a4-3e2b2621666c" />



## Validation
After the pipeline runs, the loaded tables are checked in SQL Server to make sure the cleaned data was inserted correctly and invalid records were removed.
