# CRUD_REST_APIs
## CRUD REST APIs with Python-Flask and MongoDB  

In this app, I design CRUD (create, read, update, delete) REST APIs with Python-Flask and MongoDB.

MongoDB will have database of users with fields - id, name, email and password.

The application provides the following REST API endpoints:    
    GET /users - Returns a list of all users.  
    GET /users/<id> - Returns the user with the specified ID.  
    POST /users - Creates a new user with the specified data.  
    PUT /users/<id> - Updates the user with the specified ID with the new data.  
    DELETE /users/<id> - Deletes the user with the specified ID.  

1. At first install Anaconda and Postman and MongoDB.
2. Create local environment:
   - conda create -n restapi python=3.9 
   - activate restapi 
3. Install dependencies
   - pip install flask
   - pip install pymongo
4. Start MongoDB Server
5. Start the application
   - python app.py

Once the application is started, go to localhost on Postman and test the APIs.
To test create and update key value pair should be provided for name, email and password.

