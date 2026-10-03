from sqlalchemy import create_engine, text

connection_url = (
    "mssql+pyodbc://@localhost/CustomerTransactionDB"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&trusted_connection=yes"
    "&TrustServerCertificate=yes"
)

engine = create_engine(connection_url)

with engine.connect() as connection:
    result = connection.execute(text("SELECT @@VERSION"))
    print(result.fetchone())