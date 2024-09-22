# Data Engineering Project
## Project Description
To build a data pipeline that extract the current weather data for Georgetown, Guyana from Open Weather map API, and load it to Amazon S3 using Apache Airflow installed on an Amazon EC2 machine.
<br></br>


## Tools
Amazon EC2, Amazon S3, Python, Apache Airflow
<br></br>


## Architecture Diagram
![architecture_diag2](https://github.com/user-attachments/assets/2f173ffe-8b5e-4da4-97e6-07161a6a0eab)
<br></br>

## Tools and Resaources
Amazon EC2, Amazon S3, Python, Apache Airflow
<br></br>


## Development Process
1.	Create an Amazon S3 bucket - the S3 bucket is used to store the transformed dataset
2.	Launch an Amazon EC2 instance - Select the instance that contain Ubuntu2. Select an instance Type that is T2.medium machine to ensure it has enough resources to run Airflow. This server will be used as the ETL server
3.	Install Python, PIP and the required libraries (Pandas, Airflow, S3FS etc.) on the EC2 instance
4.	Develop the following three (3) tasks in the Airflow Python script (**see script)
    - Write a task to verify that connection can be established with the Open Weather API data source
    - Write a task to extract the data from the data source to the ETL server
    - Write a task to transform and load the data to an Amazon S3 bucket

5. Arrange the tasks such that they execute sequentially from task 1 to task 3.
6. Run the Airflow job to execute the ETL process and check if it completes successfully (**see Airflow DAG)
7. Identify and troubleshoot any issues with any of the tasks and rerun the job until all the tasks are executed successfully.
8. The final output should be a CSV file in the S3 bucket containing the data extracted from the source.
<br></br>


## Airflow Directed Acyclic Graph (DAG)
![airflow_DAG](https://github.com/user-attachments/assets/cb8a499a-d1da-4179-bf11-695ed81539aa)
<br></br>

