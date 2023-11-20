# Real-time-graph-data-analytics

This project is mainly about creating a highly scalable and highly available data processing pipeline that takes a document stream as its input and performs various processing operations on it before streaming it into a distributed neo4j setup to allow for near real-time processing and analytics.

Neo4j is a scalable graph database that can store, update, and retrieve graph-structured data. This project consists of two phases. Phase 1 focuses on creating Docker containers that install Neo4j and implement two graph algorithms. Docker is an open-source platform for developing, shipping and running applications. It can be used to create standardized environments that are easily shared across teams and platforms, streamlining development and deployment.

Because the application will be used by multiple users simultaneously during peak hours, load balancing is essential to prevent database failures. Kubernetes and Apache Kafka are recommended for load balancing in this project to handle the high volume of data transactions. Kubernetes can manage and scale Docker containers running the application, ensuring that it is always available and responsive, especially during traffic spikes. Kafka can be used to stream requests and responses from users to the application.

Phase 2 of the project streamlines and tests the entire system end-to-end to ensure that data flows correctly through Kafka and that Neo4j is able to store and retrieve the data.
