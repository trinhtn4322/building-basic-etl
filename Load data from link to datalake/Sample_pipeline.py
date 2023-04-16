import pandas as pd
from pathlib import Path
from datetime import timedelta
from prefect import flow, task
from prefect.tasks import task_input_hash
from pyspark.sql import SparkSession

@task(retries=3,cache_key_fn=task_input_hash, cache_expiration = timedelta(days=1))
def extract(url) -> pd.DataFrame:
    df=pd.read_csv(url)
    return df

@task(log_prints=True)
def transform(df):
    most_frequent_value1 = df['Ngành cấp I'].value_counts().idxmax()
    most_frequent_value2 = df['Lý do'].value_counts().idxmax()
    df['Ngành cấp I'] = df['Ngành cấp I'].fillna(value=most_frequent_value1)
    df['Lý do'] = df['Lý do'].fillna(value=most_frequent_value2)
    median = df['Mã số thuế'].median()
    df = df.fillna({'Mã số thuế': median})
    df['Ngày giải thể'] = pd.to_datetime(df['Ngày giải thể'])
    return df
@task()
def local(df: pd.DataFrame, number, dataset_file:str) -> Path:
    path=Path(f"datalake/{number}/{dataset_file}.parquet")
    print(path)
    df.to_parquet(path)

    return path

@task(log_prints=True, retries=3)
def load(path: str, number: int, data: str):
    spark = SparkSession.builder.appName("Load CSV to Hadoop").getOrCreate()
    path = f"{path}"
    df = spark.read.parquet(path)
    print(path)
    hdfs_parquet_path = f"hdfs://localhost:9000/datalake/{number}/{data}.parquet"
    df.write.parquet(hdfs_parquet_path, mode="append")
@flow()
def etl_to_hadoop(number: int) -> None:
    dataset_file = f"datasample_number_{number}"
    url ="https://opendata.hochiminhcity.gov.vn/sites/default/files/DanhSachDaGiaiThe.csv"
    df=extract(url)
    df_clean=transform(df)
    path=local(df_clean,number,dataset_file)
    load(path,number,dataset_file)

@flow()
def etl_parent_flow(number: list[int] = [1, 2]):
    for num in number:
        etl_to_hadoop(num)
if __name__ == '__main__':
    number=[1,2,3]
    etl_parent_flow(number)

