# Real-time-graph-data-analytics

This project is centered around the development of a robust, highly scalable, and highly available data processing pipeline. The pipeline takes a continuous stream of documents as input, undergoes various processing operations, and seamlessly integrates with a distributed Neo4j setup for near real-time processing and analytics.

The project unfolds in two phases. In Phase 1, we focus on the implementation of Docker containers for installing Neo4j and incorporating two graph algorithms. Docker, as an open-source platform, facilitates the creation of standardized environments, enhancing collaboration across teams and platforms for efficient development and deployment.

Given the concurrent usage during peak hours, load balancing becomes critical to avoid database failures. For effective load balancing, Kubernetes and Apache Kafka are recommended. Kubernetes efficiently manages and scales Docker containers, ensuring constant availability and responsiveness, particularly during periods of increased traffic. Kafka plays a pivotal role in streaming requests and responses from users to the application.

Moving to Phase 2, the project streamlines and rigorously tests the entire system end-to-end. This ensures seamless data flow through Kafka and validates Neo4j's ability to store and retrieve data accurately.
