  * Authentication Methods *

There are many web authentication methods and tools:
Username/email and password
Using classic HTTP Basic and Digest Authentication

API key
An opaque long string with an accompanying secret

OAuth211

A set of standards for authentication and authorization

JavaScript Web Tokens (JWT)

An encoding format containing cryptographically signed user information
In this section, I’ll review the first two methods and show you how to traditionally
implement them. But I’ll stop before filling out the API and database code. Instead,
we’ll fully implement a more modern scheme with OAuth2 and JWT. /*




full layout of the project

/my_fastapi_app
|-- app/
|   |-- __init__.py
|   |-- main.py          # Entry point of the application
|   |-- config/          # Configuration settings
|   |   |-- __init__.py
|   |   |-- config.py    # Configuration parameters (e.g., secrets, database URL, Kafka brokers)
|   |-- database/        # Database related operations
|   |   |-- __init__.py
|   |   |-- base.py      # Database session and base model
|   |   |-- session.py   # Database connection and session management
|   |-- models/          # Database models (tables)
|   |   |-- __init__.py
|   |   |-- user.py      # User model
|   |-- schemas/         # Pydantic models for request and response data structures
|   |   |-- __init__.py
|   |   |-- user.py      # User schemas for serialization
|   |-- routes/          # Endpoints of the application
|   |   |-- __init__.py
|   |   |-- user.py      # User-related routes
|   |-- security/        # Authentication and security related operations
|   |   |-- __init__.py
|   |   |-- auth.py      # OAuth2 with JWT for authentication and authorization
|   |-- messaging/       # Kafka producers and consumers
|   |   |-- __init__.py
|   |   |-- producer.py  # Kafka message producer
|   |   |-- consumer.py  # Kafka message consumer
|   |-- protobufs/       # Protocol Buffer definitions and compilations
|   |   |-- __init__.py
|   |   |-- user_pb2.py  # Compiled Protocol Buffer for user data
|   |-- email/           # Email sending functionality
|   |   |-- __init__.py
|   |   |-- sender.py    # Functions to send emails
|   |-- notifications/   # Notification handling
|   |   |-- __init__.py
|   |   |-- handler.py   # Manage and send notifications to users
|   |-- utils/           # Utility functions and classes
|   |   |-- __init__.py
|   |   |-- common.py    # Common utility functions
|-- tests/
|   |-- __init__.py
|   |-- test_main.py     # Tests for your application
|-- .env                 # Environment variables



