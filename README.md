# MyApp Part 1: Data Collector

PiTemp is a complex application that consists of three parts (PiTemp, mysql_db Docker container, Java API written in Spring Web. This README file specifically covers Part 1, the Data Collector component, which is a simple Python application. This component is designed to be containerized using Docker and will connect to a MySQL container within the Docker local network to store data in a database.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Dockerization](#dockerization)
6. [MySQL Configuration](#mysql-configuration)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

MyApp is a multi-part application designed to perform various tasks efficiently. Part 1, the Data Collector, is responsible for gathering data and storing it in a MySQL database running in a separate Docker container. This simple Python application will fetch data from different sources and populate the database for further processing by other components.

## Features

- Fetch data from various sources.
- Store data in a MySQL database using Docker's local network for seamless connectivity.
- Simple and easy-to-understand Python codebase.

## Prerequisites

Before setting up and running the Data Collector, make sure you have the following installed on your system:

- Python (version 3.x)
- Docker

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your_username/myapp-data-collector.git
cd myapp-data-collector
```

Remember to change your database hostname/IP address, username, password and database in use

```
DB schema:
table name: temp_mon

+-------+--------------+------+-----+-------------------+-------------------+
| Field | Type         | Null | Key | Default           | Extra             |
+-------+--------------+------+-----+-------------------+-------------------+
| id    | datetime     | NO   | PRI | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| temp  | decimal(5,2) | YES  |     | NULL              |                   |
+-------+--------------+------+-----+-------------------+-------------------+
```

## Dockerization

To containerize the Data Collector component with Docker, follow these steps:

1. Build the Docker image:

```
docker build -t myapp-data-collector .
```

2. Run the container:

```
docker run --name data-collector-container --network myapp-network -d myapp-data-collector
```

Replace `myapp-network` with the name of your Docker local network that also connects to the MySQL container.

## MySQL Configuration

The Data Collector component requires a MySQL database to store the collected data. Ensure you have a MySQL Docker container running and appropriately configured. The Python application will use the provided database connection details (host, port, username, password) to establish a connection and store data.

## Contributing

We welcome contributions to improve MyApp and its various components. If you find any issues or want to add new features, feel free to create a pull request.

## License

MyApp is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute this code as per the terms specified in the license.

For the documentation of other parts of the MyApp, please refer to their respective README files.
