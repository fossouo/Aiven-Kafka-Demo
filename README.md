
## Introduction

Apache Kafka is a popular distributed event streaming platform used by many organizations for real-time data processing and analytics. Aiven Kafka is a managed Kafka service that provides a reliable and scalable solution without the operational overhead. In this guide, we will explore how to work with Aiven Kafka and set up observability using Grafana with InfluxDB as the data storage for monitoring and visualization.

## Prerequisites

To follow along with this guide, you will need the following:

1. An Aiven Kafka service instance: If you don't have one, sign up for Aiven at [aiven.io](https://aiven.io) and create a new Kafka service.
2. A Grafana instance: You can install Grafana locally or use a cloud-hosted Grafana service.
3. An InfluxDB instance: You can install InfluxDB locally or use a cloud-hosted InfluxDB service.

## Step 1: Set Up Aiven Kafka

1. Access your Aiven console and navigate to your Kafka service.

![plot](./images/kafkaservice_homepage.png)

2. Note down the connection details, including the **service URI**, **port**, **username**, and **password**. These will be required to connect to your Kafka cluster.

![plot](./images/download_certificates.png)

## Step 2: Produce Messages to Aiven Kafka (Local Setup) 

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
   For complete code refer to this link : [Aiven Python Kafka Producer](./kafka_producer_aiven.py)

4. Consume Messages From Aiven UI in JSON format :

   ![plot](./images/fetch_messages.png)

## Step 3: Set Up InfluxDB

1. Access your InfluxDB instance and create a new database for storing Kafka metrics.

![plot](./images/influxDBService_Running.png)

2. Integration with Kafka to collect Metrics 

![plot](./images/LogIntegration_InfluxDB.png)

3. Integration with Grafana to visualize the Metrics 

![plot](./images/LogIntegration_Grafana.png)

4. Note down the connection details, including the **host**, **port**, **username**, **password**, and **database name**. 

## Step 4: Set Up Grafana for Observability

1. Install Grafana following the official documentation of Aiven.

2. Access the Grafana web interface using your browser and log in with your credentials.

![plot](./images/GrafanaService_homepage.png)

3. Click on "Integrations" in the side menu and select "Receive Data".

![plot](./images/GrafanaService_InfluxDB_Integration.png)

4. When the Integration is complete you will see it in the default page.

![plot](./images/GrafanaService_Integrations.png)

## Step 5: Create Kafka Dashboards

1. Click on "Home Page" in the side menu and select "Dashboard".

2. Click on "Browse" and select the Kafka Aiven - Kafka Metrics.

![plot](./images/InfluxDB_Grafana_homepage.png)

3. Validate and Create the Dashboard. 

![plot](./images/InfluxDB_Grafana.png)

4. Customize the dashboard by adding panels, visualizations, and additional queries as needed.

5. Save the dashboard and give it a meaningful name.

## Conclusion

In this guide, we walked through the process of working with Aiven Kafka and setting up observability using Grafana with InfluxDB as the data storage for monitoring and visualization. We learned how to connect to Aiven Kafka using Python, set up InfluxDB as a data source in Grafana, and create Kafka dashboards for monitoring Kafka metrics.

By following these steps, you can ensure the reliability and performance of your Kafka infrastructure while gaining insights into your streaming data using powerful visualization capabilities provided by Grafana with InfluxDB as the data source.

Remember to refer to the Aiven, Grafana, and InfluxDB documentation for more advanced configuration options and features.

- Kafka : https://docs.aiven.io/docs/products/kafka 
- Grafana : https://docs.aiven.io/docs/products/grafana 
- InfluxDB : https://docs.aiven.io/docs/products/influxdb 
