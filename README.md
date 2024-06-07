# LucidTask Web Application

This project is a web application built using the MVC design pattern, Python, FastAPI, and SQLAlchemy for ORM. It interfaces with a MySQL database and implements field validation, dependency injection, and token-based authentication. The application features endpoints for user signup, login, adding posts, fetching user posts, and deleting posts. Response caching is used to optimize the retrieval of user posts.

## Functional Tasks

1. **User Signup**
   - Endpoint: `/signup/`
   - Method: `POST`
   - Accepts `email` and `password`
   - Returns a JWT token for authentication

2. **User Login**
   - Endpoint: `/login/`
   - Method: `POST`
   - Accepts `email` and `password`
   - Returns a JWT token upon successful login

3. **Add Post**
   - Endpoint: `/addpost/`
   - Method: `POST`
   - Accepts `text` and a JWT token for authentication
   - Validates payload size (limit to 1 MB)
   - Saves the post and returns `postID`

4. **Get Posts**
   - Endpoint: `/getposts/`
   - Method: `GET`
   - Requires a JWT token for authentication
   - Returns all user's posts
   - Implements response caching for up to 5 minutes

5. **Delete Post**
   - Endpoint: `/deletepost/{post_id}/`
   - Method: `DELETE`
   - Accepts `postID` and a JWT token for authentication
   - Deletes the corresponding post

## Setup Instructions

1. **Clone the Repository**
   ```sh
   git clone git@github.com:RichardKaranuMbuti/LucidTask.git
   cd LucidTask

## Create and Activate Virtual Environment
sh
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

## Install Dependencies 
sh
pip install -r requirements.txt


## Create a .env file in the project root and add the following variables:

environment = "development"
### DB Credentials
db_password = <your_db_password>
db_user = <your_db_user>
db_host = <your_db_host>
db_name = <your_db_name>
db_port = <your_db_port>
security_key = <your_security_key>

## Run Database Migrations

python manage.py makemigrations
python manage.py migrate

## Initialize the Database

python init.db.py

## Start the Server

uvicorn core.fastapi_app:app --reload

## API Endpoints and Testing

## Signup Endpoint:
POST /signup/
### Body (JSON):
json
{
 "email": "user@example.com",
 "password": "password123"
}
### Response: Returns a JWT token for the authenticated user.

## Login Endpoint:
POST /login/
### Body (JSON):
json
{
 "email": "user@example.com",
 "password": "password123"
}
### Response: Returns a JWT token upon successful login.

## Add Post Endpoint:
POST /addpost/
### Headers:

Authorization: Bearer <your_token>

### Body (JSON):
json
{
 "text": "This is a new post"
}
### Response: Saves the post and returns the postID.

## Get Posts Endpoint:
GET /getposts/
### Headers:

Authorization: Bearer <your_token>

### Response: Returns all user's posts. Implements response caching for up to 5 minutes.

# Delete Post Endpoint:
DELETE /deletepost/{post_id}/
### Headers:

Authorization: Bearer <your_token>

## Response: Deletes the corresponding post and returns a success message.

