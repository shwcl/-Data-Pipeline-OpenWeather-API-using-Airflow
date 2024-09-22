# Data Engineering Project
## Project Description
To build a data pipeline that extract the current weather data for Georgetown, Guyana from Open Weather map API, and load it to Amazon S3 using Apache Airflow installed on an Amazon EC2 machine.
<br></br>

## Tools
Amazon EC2, Amazon S3, Python, Apache Airflow


## Architecture Diagram

![airflow_DAG](https://github.com/user-attachments/assets/8b221a03-9442-4dcf-bb4b-42d42fbd3a15)





## Tools and Resaources
Amazon EC2, Amazon S3, Python, Apache Airflow

<br></br>

## Development Process
1.	Create an Amazon S3 bucket - the S3 bucket is used to store the transformed dataset
2.	Launch an Amazon EC2 instance - Select the instance that contain Ubuntu2. Select an instance Type that is T2.medium machine to ensure it has enough resources to run Airflow. This server will be used as the ETL server
3.	Install Python, PIP and the required libraries (Pandas, Airflow, S3FS etc.) on the EC2 instance
4.	Develop the tasks and workflow in Airflow to execute the ETL process

Execute the following tasks:
1.	 Verify that a connection can be established with the Open Weather API data source
2.	 Extract the data from the data source to the ETL server
3.	 Transform and load the data to an Amazon S3 bucket

-	Run the Airflow job to execute the ETL process.
-	 Check that each task completes successfully.
-	 Identify and troubleshoot any issues with any of the tasks and rerun the job until all the tasks are executed successfully.
-	 The final output should be a CSV file in the S3 bucket containing the data extracted from the source.
