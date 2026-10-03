import pandas as pd
from sqlalchemy import create_engine

def extract_data(): 
    df_customers = pd.read_csv("customers.csv")
    df_transactions = pd.read_csv("transactions.csv")
    df_products = pd.read_csv("products.csv")
    return df_customers, df_transactions, df_products

def Transform_customer(customer):
    customer["email"] = customer["email"].astype("string").str.strip()

    valid_email = customer["email"].str.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", na=False) # __@__.__ or nan -> false
    customer.loc[~valid_email, "email"] = pd.NA
    return customer

def Transform_transaction(transaction):
    transaction["transaction_date"] = pd.to_datetime(transaction["transaction_date"], format="%d/%m/%Y", errors="coerce")
    transaction = transaction.drop_duplicates(subset=["transaction_id"], keep="first")
    return transaction

def Transform_product(product):
    product["category"] = product["category"].astype("string").str.strip().str.lower().str.title()
    return product

def load_data_to_sql(customers, transactions, products):
    connection_url = (
    "mssql+pyodbc://@localhost/CustomerTransactionDB"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&trusted_connection=yes"
    "&TrustServerCertificate=yes"
    )

    engine = create_engine(connection_url)
    # customers.to_sql("customers",con=engine,if_exists="append",index=False)
    transactions.to_sql("transactions",con=engine,if_exists="append",index=False)
    # products.to_sql("products",con=engine,if_exists="append",index=False)
    

def main():
    customers, transactions, products = extract_data()
    customers = Transform_customer(customers)
    transactions = Transform_transaction(transactions)
    products = Transform_product(products)
    load_data_to_sql(customers, transactions, products)
    print(customers["email"])
    print("finish")

if __name__ == "__main__":
    main()