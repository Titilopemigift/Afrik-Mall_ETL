# Extract Data from faker

import pandas as pd
import random

# Generate unique transaction IDs
def generate_unique_ids(num_records):
    return random.sample(range(10, 10000), num_records) 

# Create fake sales data
from faker import Faker

fake = Faker()
num_records = 5000  
transaction_ids = generate_unique_ids(num_records) 

sales_data = []
for i in range(num_records):
    sales_data.append({
        "transaction_id": transaction_ids[i],  # Assign a unique ID
        "customer_name": fake.name(),
        "product": fake.word(),
        "amount": round(fake.random_number(digits=4), 2),
        "date": fake.date_this_year()
    })
#save to csv
df = pd.DataFrame(sales_data)
df.to_csv("sales_data.csv", index=False)

print("Data generated with unique transaction IDs")
print(df)

#  Transform data

df = pd.read_csv("sales_data.csv")

# Standardize column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Drop duplicates
df = df.drop_duplicates()

df.to_csv("cleaned_sales_data.csv", index=False)
print("Data cleaned and saved")


# Load data to postgres

import psycopg2
import pandas as pd

# Database connection
import getpass

password =getpass.getpass("your_password:")
print ("password secured")

conn = psycopg2.connect (
    
   host = "localhost",
   database = "afrik_mall",
   port = 5432,
   user = "postgres",
   password = password
)

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS sales_data (
    transaction_id INT PRIMARY KEY,
    customer_name TEXT,
    product TEXT,
    amount NUMERIC,
    date DATE
);
""")
conn.commit()

# Load data
df = pd.read_csv("cleaned_sales_data.csv")
for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO sales_data (transaction_id, customer_name, product, amount, date) VALUES (%s, %s, %s, %s, %s)",
        (row["transaction_id"], row["customer_name"], row["product"], row["amount"], row["date"])
    )

conn.commit()
cur.close()
conn.close()

print("Data successfully loaded into PostgreSQL")


