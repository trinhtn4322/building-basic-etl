# Using conda to mix virtual environment

- Allows to install packages and libraries for each project
- Easy to manage

--- conda create -n demo python=3.9

--- conda activate demo

- import requirment libraries

--- pip install -r library.txt
# Start using prefect
--- from perfect import flow, task
- Flow is an object representing a Prefect workflow, defined by a Python function.
- Task is an object that represents a task in the Prefect workflow, defined by a Python function.

# Data Lake
- Use pyspark to put data into data lake, specifically here is Hadoop
- Data is distinguished by directory datalake/{number}/datasample_{number}.parquet
-![image](https://user-images.githubusercontent.com/115331941/232331807-31589ada-ac5b-4a4c-bb20-9f6582ee8ba1.png)
