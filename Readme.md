# Deepchecks Backend with FastAPI

## Project Description

This project is a backend service built with FastAPI to log interactions, calculate metrics, and set up alerts based on metric values. The service includes:
- Logging new interactions
- Retrieving interactions and their calculated metrics
- Setting up alerts based on metric values:
  - Threshold Alert: Triggered when a metric value exceeds a specified threshold.
  - Outlier Alert: Triggered when a metric value is significantly different from other values (outlier detection).
- Querying alerts, which return details on activated alerts, including the specific interaction and element involved.


## Setup Instructions

### Prerequisites

- Docker
- Docker Compose
- Python 3.9+
- Postman (for API testing)

### Environment Variables

Create a `.env` file in the root directory of the project by doing:

```env
`cp .env.example .env`
```

## Building and Running the Application

### 1. Ensure the .env file is configured correctly:
Make sure your .env file contains the correct values for your environment.

### 2. Build and start the containers:
```bash
docker-compose up --build
```
### 3. Run the simulation script:
```bash
python simulate_llm.py
```

## Using Postman Collection
1. Open Postman.
2. Import the provided Postman collection `FastAPI.postman_collection.json.`
3. The collection includes pre-configured requests for:
    -  Logging new interactions
    - Retrieving metrics
    - Querying alerts