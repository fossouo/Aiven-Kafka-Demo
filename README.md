
**Title: Working with Aiven Kafka and Observability: A Step-by-Step Guide**

## Introduction

Apache Kafka is a popular distributed event streaming platform used by many organizations for real-time data processing and analytics. Aiven Kafka is a managed Kafka service that provides a reliable and scalable solution without the operational overhead. In this guide, we will explore how to work with Aiven Kafka and set up observability using Grafana for monitoring and visualization.

## Prerequisites

To follow along with this guide, you will need the following:

1. An Aiven Kafka service instance: If you don't have one, sign up for Aiven at [aiven.io](https://aiven.io) and create a new Kafka service.
2. A Grafana instance: You can install Grafana locally or use a cloud-hosted Grafana service.

## Step 1: Set Up Aiven Kafka

1. Access your Aiven console and navigate to your Kafka service.
2. Note down the connection details, including the **service URI**, **port**, **username**, and **password**. These will be required to connect to your Kafka cluster.

![Aiven Console](screenshots/aiven_console.png)

## Step 2: Connect to Aiven Kafka

1. Install the `kafka-python` library using the following command:
   ```
   pip install kafka-python
   ```
   
2. Open a Python script or Jupyter Notebook and import the necessary libraries:
   ```python
   from kafka import KafkaProducer, KafkaConsumer
   ```

3. Set up a Kafka producer to send messages to your Kafka topic:
   ```python
   producer = KafkaProducer(
       bootstrap_servers='<service_uri>:<port>',
       security_protocol='SSL',
       ssl_cafile='/path/to/ca.pem',
       ssl_certfile='/path/to/service.cert',
       ssl_keyfile='/path/to/service.key'
   )

   producer.send('<topic>', value=b'Hello, Kafka!')
   producer.flush()
   ```
   Complete code is available in github repo : kafka_producer_aiven.py


## Step 3: Set Up Grafana for Observability

1. Install Grafana following the official documentation for your platform.

2. Access the Grafana web interface using your browser and log in with your credentials.

3. Click on "Configuration" in the side menu and select "Data Sources".

4. Click on "Add data source" and select "Kafka" from the list.

5. Configure the Kafka data source by providing the connection details:
   - Name: Enter a name for the data source.
   - Kafka server: Enter the **service URI** for your Aiven Kafka cluster.
   - Kafka port: Enter the Kafka port (default is 9092).
   - SASL username and password: Enter your Aiven Kafka credentials.
   - SSL: Enable SSL and provide the paths to your SSL certificates.

   ![Grafana Data Source](screenshots/grafana_data_source.png)

6. Click on "Save & Test" to verify the connection to your Aiven Kafka cluster.

## Step 4: Create Kafka Dash

boards

1. Click on "Create" in the side menu and select "Dashboard".

2. Click on "Add query" and select the Kafka data source you configured.

3. Write a query to retrieve Kafka metrics. For example, to monitor the Kafka consumer lag, you can use the following query:
   ```sql
   SELECT "value" FROM "consumer_lag" WHERE "group_id" = '<consumer_group_id>'
   ```

   ![Grafana Dashboard](screenshots/grafana_dashboard.png)

4. Customize the dashboard by adding panels, visualizations, and additional queries as needed.

5. Save the dashboard and give it a meaningful name.

## Conclusion

In this guide, we walked through the process of working with Aiven Kafka and setting up observability using Grafana with InfluxDB as the data storage for monitoring and visualization. We learned how to connect to Aiven Kafka using Python, set up InfluxDB as a data source in Grafana, and create Kafka dashboards for monitoring Kafka metrics.

By following these steps, you can ensure the reliability and performance of your Kafka infrastructure while gaining insights into your streaming data using powerful visualization capabilities provided by Grafana with InfluxDB as the data source.

Remember to refer to the Aiven and Grafana documentation for more advanced configuration options and features.
https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
https://help.aiven.io/en/articles/489587-getting-started-with-aiven-grafana 
