# ROS 2 Nodes, Topics, and Services

ROS 2 (Robot Operating System 2) is a flexible framework for writing robot software. It's designed to build complex and robust robot applications across a wide variety of robotics platforms.

## ROS 2 as Middleware for Robot Control

At its core, ROS 2 provides a middleware layer that enables different components of a robot system to communicate with each other. This communication is essential for coordinating sensors, actuators, and decision-making processes.

## Key Concepts

### 1. Nodes

A **Node** is an executable process that performs computation. In a ROS 2 system, individual functionalities (like a camera driver, a motor controller, or a path planner) are typically encapsulated into nodes. Nodes communicate with each other using ROS topics, services, or actions.

### 2. Topics

**Topics** are a fundamental communication mechanism in ROS 2. They are used for asynchronous, many-to-many communication. When a node wants to share information, it publishes messages to a topic. Other nodes interested in that information subscribe to the topic.

*   **Publishers**: Nodes that send messages to a topic.
*   **Subscribers**: Nodes that receive messages from a topic.

**Example**: A camera node might publish image data to an `/image` topic, and an image processing node would subscribe to that topic to receive and process the images.

### 3. Services

**Services** provide a request/reply communication pattern. Unlike topics, which are asynchronous and one-way, services are synchronous and bidirectional. A client node sends a request to a service, and the service node processes the request and sends back a response.

*   **Service Server**: A node that provides a service and waits for requests.
*   **Service Client**: A node that requests a service from a service server.

**Example**: A navigation client might request a path from a navigation service. The navigation service calculates the path and returns it as a response.
