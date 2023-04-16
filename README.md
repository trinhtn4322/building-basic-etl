# Using Docker
- This whole project is made based on Docker, pre-installed postgres, pgadmin, spark, hive, hadoop

![image](https://user-images.githubusercontent.com/115331941/232332014-55aa0ace-0b19-44ae-84de-f7a2e35eb03c.png)

# building-basic-etl
- ETL stands for Extract, Transform, and Load. It is a process used in data integration and data warehousing to extract data from one or more sources, transform it to fit business needs and load it into a target system, such as a data warehouse or a data lake.
- Data warehouses are typically used for storing historical data, and they are designed to support complex queries and analytics with high performance and reliability.
- On the other hand, a data lake is a decentralized repository that stores both structured and unstructured data from different sources, without any predefined schema or structure. Data lakes are designed to store raw and unprocessed data at scale, and they are optimized for flexibility, agility, and exploration. Data lakes enable organizations to store all types of data in their original format, without the need for upfront transformation, which can be expensive and time-consuming. Data lakes are typically used for data exploration, data science, and machine learning.

# Dataset
- Because I have not had access to the real database, it is difficult for me to extract from an actual database
- I will replace it with a data set called Danhsachgiaithe.csv
- I'm going to create a fake ETL pipeline to automate data extraction and inclusion in the data lake
- Source : https://opendata.hochiminhcity.gov.vn/
- Link of the data : https://opendata.hochiminhcity.gov.vn/sites/default/files/DanhSachDaGiaiThe.csv

# [Check_data](.trinhtn4322/building-basic-etl/Check-data/)

- In this part, I will download a data sample
- The first step I will use Jupyter Notebook to check what is this data set has?
- Then I will conduct analysis and clean it

# Create a simple pipeline
- Create Docker-compose.yaml to run postgres and pgadmin
- Connecting pgAdmin and Postgres
- Create engine in Jupyter notebook and connect to prostgresql
- Build a simple pipline load data to PgAdmin
- Finally, converting the Jupyter notebook to a Python script

# Building a pipeline to load data from link to datalake

- The pipeline is built using the Prefect library, which provides a framework for building, scheduling, and monitoring data workflows. The pipeline has three main tasks:

- extract: reads data from the CSV file at the specified URL and returns a Pandas DataFrame.
- transform: cleans and manipulates the DataFrame returned by extract.
- load: loads the transformed data into HDFS in Parquet format using Apache Spark.
