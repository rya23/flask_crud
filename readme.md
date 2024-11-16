# **Flask CRUD API**

This is a simple CRUD (Create, Read, Update, Delete) REST API built using **Flask**, **MongoDB**. The API allows managing users, providing endpoints for creating, reading, updating, and deleting users.

## **Features**

-   Perform CRUD operations on `User` resources.
-   MongoDB integration for data persistence.
-   Containerized with Docker.
-   Pydantic for Data Val

---

## **API Endpoints**

API Endpoints
Retrieve All Users

    Method: GET
    Endpoint: /users
    Description: Returns a list of all users.

Create a New User

    Method: POST
    Endpoint: /user
    Description: Creates a new user with the provided name, email, and password.

Retrieve a User by ID

    Method: GET
    Endpoint: /user/<id>
    Description: Retrieves the user with the specified unique ID.

Update a User by ID

    Method: PUT
    Endpoint: /user/<id>
    Description: Updates the user with the specified unique ID. Requires updated name, email, or password in the request body.

Delete a User by ID

    Method: DELETE
    Endpoint: /user/<id>
    Description: Deletes the user with the specified unique ID.

---

## **Setup and Installation**

### **Clone the Repository**

```bash
git clone https://github.com/rya23/flask_crud.git
cd flask_crud
```

### **Docker Setup**

#### **Environment Variables**

Create a `.env` file in the project root and define the MongoDB connection string:

```
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database-name>
```

#### **Build and Run Containers**

1. Build the Docker image:

    ```
    docker compose build
    ```

2. Start the application:

    ```
    docker compose up
    ```

3. The Flask API will be accessible at:
    ```
    http://localhost:5000/user
    ```

---

## **Project Structure**

```
.
├── app.py               # Main Flask application
├── Dockerfile           # Dockerfile for the app
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
└── .env                 # Environment variables (MongoDB URI)
```
