# Afrik-Mall-ETL-Pipeline

# Project Overview
 
The Afrik Mall ETL Pipeline is an automated data pipeline designed to extract, transform, and load (ETL) sales data into a PostgreSQL database. The dataset is generated using the Faker library, ensuring a structured and scalable approach for testing data processing workflows.

# Data Sources

Faker-Generated Dataset: Synthetic sales data created using the Faker library in Python.
CSV Files: The generated data is stored as CSV files before processing.

# Tools Used

Programming: Python

Orchestration: Apache Airflow

Database: Postgres

Data Generation: Faker(Python)

Transformation:Pandas

# ETL Process Flow

- Extract – Generate fake sales data using Faker and store it as CSV.
- Transform – Clean and normalize data using Pandas.
- Load – Store structured data in PostgreSQL.
- Monitor – Track execution via Airflow UI.

# Conclusion

The Afrik Mall ETL Pipeline successfully automates the process of extracting, transforming, and loading synthetic sales data into a structured PostgreSQL database. By leveraging Faker for data generation, Apache Airflow for orchestration, and PostgreSQL for storage, this project demonstrates an efficient approach to handling ETL workflows.

This pipeline can be extended to support real-world datasets, integrate cloud storage solutions like AWS S3, and implement real-time data processing with tools like Apache Kafka. Future improvements will focus on data validation, performance optimization, and advanced analytics to derive meaningful insights.

