CREATE DATABASE CustomerTransactionDB;
GO

use CustomerTransactionDB;

create table customers(
	customer_id varchar(255) primary key,
	name varchar(255),
	email varchar(255),
	address varchar(255)
)

create table transactions(
	transaction_id varchar(255) primary key,
	customer_id varchar(255),
	transaction_date date,
	amount decimal(18,2)

	constraint fk_transaction_customer foreign key(customer_id) references customers(customer_id)
)

create table products(
	product_id varchar(255) primary key,
	product_name varchar(255),
	category varchar(255),
	price decimal(18,2)
)

-- select * from customers
-- SELECT * from products
-- SELECT * from transactions

SELECT customer_id, SUM(amount) AS total_revenue
INTO customer_revenue
FROM transactions
GROUP BY customer_id;

SELECT * from customer_revenue
